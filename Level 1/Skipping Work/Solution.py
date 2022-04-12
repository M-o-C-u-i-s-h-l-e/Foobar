def solution(x, y):
    additionalId = 0
    for i in x:
        additionalId ^= i
    for i in y:
        additionalId ^= i
    return additionalId
