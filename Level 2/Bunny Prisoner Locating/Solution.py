def solution(x, y):
    n = x + y - 1
    ID = (n * (n-1)) >> 1
    return str(ID + x)
