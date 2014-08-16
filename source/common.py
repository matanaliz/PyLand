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


def angle(v):
    assert len(v) == 2
    return math.atan2(v[0], v[1]) * 180 / math.pi


def mul(v, c):
    assert isinstance(c, (float, int))
    return [_ * c for _ in v]