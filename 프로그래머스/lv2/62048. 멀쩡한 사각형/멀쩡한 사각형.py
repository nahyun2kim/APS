from math import gcd

def solution(w,h):
    a = gcd(w, h)
    line = w + h - a
    return w * h - line