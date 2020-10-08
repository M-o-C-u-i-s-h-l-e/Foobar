from math import sqrt
from decimal import Decimal, getcontext
getcontext().prec = 101

# Beatty Sequence Sum
def solve(n):
	if n <= 1:
		return n
	n_ = int((Decimal(2).sqrt() - 1) * n)
	return (n_ * n) + (n * (n + 1) >> 1) - (n_ * (n_ + 1) >> 1) - solve(n_)

def solution(s):
	return str(solve(int(s)))
