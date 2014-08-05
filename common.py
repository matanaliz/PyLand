__author__ = 'matanaliz'

import math

def sub(u, v):
    assert len(u) == len(v)
    return [u[i] - v[i] for i in range(len(u))]

def add(u, v):
    assert len(u) == len(v)
    return [u[i] + v[i] for i in range(len(u))]

def magnitude(v):
    return float(math.sqrt(sum(v[i]*v[i] for i in range(len(v)))))

def normalize(v):
    vmag = magnitude(v)
    return [ float(v[i])/vmag  for i in range(len(v)) ]