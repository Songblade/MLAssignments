import numpy as np


# fibonacci using recursion, with an array storing found values for efficiency
def recursive_fibonacci(n):

    def recurse(num, mem):
        if mem[num] is None:
            mem[num] = recurse(num - 1, mem) + recurse(num - 2, mem)
        return mem[num]

    if n == 0 or n == 1:
        return n
    else:
        memory = [0] + [1] + [None]*(n - 1)
        return recurse(n, memory)


# This uses a loop, with two variables (a and b) providing storage
def imperative_fibonacci(n):
    a, b = 0, 1
    if n == 0 or n == 1:
        return n
    else:
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# I learned about the matrix method at the following link:
# https://web.media.mit.edu/~holbrow/post/calculating-fibonacci-numbers-with-matrices-and-linear-algebra/
# I saw that it had Python code, though I tried not to look at it
# This is my version, using NumPy's linear algebra library
def matrix_fibonacci(n):
    if n == 0 or n == 1:
        return n
    fib_matrix = np.array([[1, 1], [1, 0]])
    current_vector = np.array([1, 0])
    for _ in range(2, n + 1):
        current_vector = np.dot(fib_matrix, current_vector)
    return current_vector[0]


print(recursive_fibonacci(12))
print(imperative_fibonacci(12))
print(matrix_fibonacci(12))

