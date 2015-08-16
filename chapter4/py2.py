#!/usr/bin/env python

A = [ [1, 2, 3],
      [4, 5, 6]] # 2 rows and 3 columns

B = [ [1, 2],
      [3, 4],
      [5, 6]]  # 3 rows, 2 columns

print A, B

# row and columns
def shape(A):
        num_rows = len(A)   # row of the matrix A
        num_columns = len(A[0]) # columns of A
        return num_rows, num_columns

def get_row(A, i):
        return A[i]

def get_column(A, j):
        return [A_i[j]      # jth element of row A_i
                    for A_i in A]   # for each row A_i

def make_matrix(num_rows, num_cols, entry_fn):
    """ return a num_rows * num_columns matrix
        whose (i,j)th entry is entry_fn(i, j) """
        return [[entry_fn(i,j)
                for j in range(num_cols)]
                for i in range(num_rows)]


def is_diagonal(i, j):
    """ 1 is on the diagonal, 0 is everywhere else"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)    # will generate the matrix using the is_diagonal fn
