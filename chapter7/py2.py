#!/usr/bin/env python
import math

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0 # normal_cdf(-10) is close to 0
    hi_z, hi_p = 10.0, 1    # normal_cdf(10) is close to 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = (low_p + hi_p) / 2

        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def normal_approximation_to_binomial(n, p):
    """ finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

def normal_upper_bound(probability, mu = 0, sigma = 1):
    """ returns the z for which p( Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu = 0, sigma = 1):
    """ return the z for which P( Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu = 0, sigma = 1):
    """ returns the symmetric(about the mean) bounds that contain the specific probability"""
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    low_bound = normal_upper_bound(tail_probability, mu, sigma)

    return low_bound, upper_bound


# do the experiment 1000 times with the p = 0.5
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# consider the case that it rejects the H_0
normal_two_sided_bounds(0.95, mu_0, sigma_0) # (469, 531)


# 95% bounds based on the assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0. sigma_0)

# now assumes that p = 0.55 based on 1000 times experiment
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error means that we fail to reject the null hypothesis, which wil happen when X is still in our original
type_2_probability = normal_probability(lo, hi, wu_1, sigma_1)
power =  1 - type_2_probability #(0.887)


# find the probability that p <= 0.5(Another case)
hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power 1 - type_2_probability


def two_sided_p_value(x, mu = 0, sigma = 1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)

# let's see the 530 heads experiment
two_sided_p_value(529.5, mu_0, sigma_0) # 0.062
# why 529.5 instead of 530? becuase of continutity correction, that
# normal_probability_between(529.5, 530.5, mu_0, sigma_0) is better than the result
# of normal_probability_between(530, 531, mu_0, sigma_0) for the estimate of the
# probability of seeing 530 heads



# to convice the above conclusion, let's run the experiment below
exterme_value_count = 0

# run the experiment for 100000 times
for _ in range(100000):
    num_heads = sum( 1 for random.random() < 0.5 else 0
                for _ in range(1000))   # count the # of heads

    if num_heads >= 530 or num_heads <= 470:    # two cases that reflect the same
        exterme_value_count += 1

print exterme_value_count / 100000  # 0.062


two_sided_p_value(531.5, mu_0, sigma_0) # 0.0463

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

# for 525 heads, the result
upper_p_value(524.5, mu_0, sigma_0) # 0.061, won't reject the null
upper_p_value(526.5, mu_0, sigma_0) # 0.047, will reject the null
