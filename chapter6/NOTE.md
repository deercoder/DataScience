NOTE
====


## Theory

1. Independent probability, which means the event `E` and event `F` are unrelated, that `E` has no information on the occurance of event `F`. So for the probability, it is **P(E,F) = P(E) * P(F)**, which means when occuring the event of E and F, they have no inference and will calculate the product of them

2. Conditional probability, that means when they're not independent, we can calculate the probability of event `F` on the condition that event `E` also occurs, we can mark it as `P(E|F)`, and we can also calculate the probability using this equation:

    P(E, F) = P(E|F) * P(F) ## the probability that counts on each other, P(E,F) means occured at the same time

3. Bayes's Theorem:

    P(E|F) = P(F|E) * P(E) / [P(F|E) * P(E) + P(F|^E) * P(^E)]
    --> from P(E|F) = P(E,F) / P(F) = P(F|E) * P(E) / P(F)

4. Continuous Distributions

    * pdf: probability density function
    * cdf: cumulative distributions function

                return 1 if x >= 0 and x < 1 else 0

            def uniform_cdf(x):
                if x < 0:
                    return 0
                elif x < 1:
                    return x
                else:
                    return 1

5. Normal distributions:

    * mean(u)
    * standard deviation (sigma)

            def normal_pdf(x, mu=0, sigma=1):
                sqrt_two_pi = math.sqrt(2 * math.pi)
                return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))
