__author__ = 'matanaliz'

import math

EPS = 0.003

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
    assert vmag - 0.0 > EPS
    return [ float(v[i])/vmag  for i in range(len(v)) ]