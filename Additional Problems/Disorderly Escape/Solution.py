from math import factorial
from collections import Counter
from fractions import gcd

def cycleCount(c, n):
	count = factorial(n)
	for i, j in Counter(c).items():
		count //= (i ** j) * factorial(j)
	return count

def cyclePartitions(n, i=1):
	yield [n]
	for i in range(i, (n>>1)+1):
		for p in cyclePartitions(n-i, i):
			yield [i] + p

def solution(w, h, s):
	res = 0
	for cpw in cyclePartitions(w):
		for cph in cyclePartitions(h):
			temp = cycleCount(cpw, w) * cycleCount(cph, h)
			res += temp * (s ** sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
	return str(res // (factorial(w) * factorial(h)))
