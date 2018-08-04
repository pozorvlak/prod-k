#!/usr/bin/env python

from sys import argv

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
        print f(int(argv[1]))
    else:
        print f(100)
