#!/usr/bin/env python

from sys import argv
from math import log
import operator
import itertools

# product(primes <=53) is greater than 2^64
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

def product(multiplicities, ps):
    prod = 1
    for m in map(operator.pow, ps, multiplicities):
        prod *= m
    return prod

def factors(multiplicities, ps):
    subsets = itertools.product(*(range(m + 1) for m in multiplicities))
    for s in subsets:
        yield product(s, ps)

def num_expressions(multiplicities, k, ps):
    "How many ways can you write 2^m1*3^m2*... as a product of numbers < k?"
    prod = product(multiplicities, ps)
    if prod > k*k:
        return 0
    min_factor = prod / k
    return len(filter(lambda x: min_factor < x < k, factors(multiplicities, ps)))

def max_index(limit, p):
    return int(log(limit, p))

def candidates(limit, max_i, ps):
    if len(ps) == 0:
        yield []
    else:
        p = ps[0]
        for i in range(min(max_index(limit, p), max_i) + 1):
            prod = p ** i
            if prod > limit:
                return
            for c in candidates(limit / prod, i, ps[1:]):
                yield [i] + c

def useful_primes(k):
    prod = 1
    ps = []
    for p in primes:
        if prod * p < k:
            prod *= p
            ps.append(p)
    return ps

def f2(k):
    max_products = 0
    best_number = 0
    count = 0
    limit = k*k
    ps = useful_primes(limit)
    for c in candidates(limit, max_index(limit, 2), ps):
        count += 1
        products = num_expressions(c, k, ps)
        if products > max_products:
            max_products = products
            best_number = product(c, ps)
    print "Considered", count, "candidates"
    return best_number, max_products

def argmax(v):
    return max(range(len(v)), key=lambda i: v[i])

def collisions(k):
    v = [0]*(k*k)
    for i in range(1, k):
        for j in range(1, k):
            v[i*j] += 1
    return v

def f(k):
    v = collisions(k)
    x = argmax(v)
    return x, v[x]

if __name__ == '__main__':
    if len(argv) > 1:
        print f2(int(argv[1]))
    else:
        print f2(2**64)
