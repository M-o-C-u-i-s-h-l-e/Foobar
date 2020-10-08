def solution(s):
	n = len(s)
	for i in range(1, (n >> 1)+1):
		l, r = i, n // i
		if l * r == n:
			flag = True
			subStr = s[: l]
			for j in range(l, n-l+1, l):
				if not s[j: j+l] == subStr:
					flag = False
					break
		if flag:
			return r
	return 1
