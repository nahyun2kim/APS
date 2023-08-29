def solution(absolutes, signs):
    return sum([a * (1 if s else -1) for a, s in zip(absolutes, signs)])