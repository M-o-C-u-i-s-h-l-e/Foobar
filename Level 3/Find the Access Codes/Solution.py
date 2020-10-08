def solution(l):
    def solution(l):
    n = len(l)
    divisor = [0] * n   # To count no. of elements that are divided by cur element
    dividend = [0] * n  # To count no. of elements that divides the cur element
    for i in range(n):
        for j in range(i+1, n):
            if (l[j] % l[i] == 0):
                divisor[i] += 1
                dividend[j] += 1
    return sum(divisor[i] * dividend[i] for i in range(n))
