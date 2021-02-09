"""
Implementation of the Fibonacci numbers in various versions.
"""


# recursive: easy to code from the definition of Fibonacci numbers but
# gets very slow for larger numbers of n. Try 40
def fibr(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibr(n - 1) + fibr(n - 2)


# iterative: much faster then the recursive version and consumes a small amount
# of constant memory in contrast to the growing memory consumption of the
# recursive version.
# However, not necessarily easy to come up with an iterative solution if
# the problem is inherently recursive
def fibi(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


# memoization/caching: an easy way to make a recursive implementation faster
# and less memory hungry, if the recursive implementation contains
# unnecessary dublicate computations.
def fibc(n, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    cache[n] = fibc(n - 1) + fibc(n - 2)
    return cache[n]


# closed-form: the fastest way to a single compute Fibonacci number.
# But OverflowError since floats are used and no automatic
# switch to "bignum" integer type can occur
# https://stackoverflow.com/questions/538551/handling-very-large-numbers-in
# -python
def fibg(n):
    from math import sqrt
    s5 = sqrt(5)
    return round(((1 + s5) ** n - (1 - s5) ** n) / (2 ** n * s5))


# closed-form: here we use Decimal to overcome the OverflowError
def fibgd(n):
    import decimal
    decimal.getcontext().prec = 1000
    sqrt5 = decimal.Decimal(5).sqrt()
    return round(((1 + sqrt5) ** n - (1 - sqrt5) ** n) / (2 ** n * sqrt5))


if __name__ == '__main__':
    n = 30
    print(fibc(n))
    print(fibi(n))
    print(fibg(n))
    print(fibgd(n))
    print(fibr(n))  # this will be very slow for n > 40
