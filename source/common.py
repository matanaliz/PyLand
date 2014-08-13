# -*- coding: utf-8 -*-
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
    return float(math.sqrt(sum(v[i] * v[i] for i in range(len(v)))))


def normalize(v):
    mag = magnitude(v)
    if mag - 0.0 < EPS:
        mag = EPS
    return [float(v[i]) / mag for i in range(len(v))]