def solution(n):
	n = int(n)
	mem = {1: 0, 2: 1}  # Memorization Table
	st = []
	st.append(n)
	while len(st):
		n = st[-1]
		if n in mem:    # If cur elment is already visited
			st.pop()
		elif n % 2 == 0:    # If cur element is Even
			if (n >> 1) in mem: # If cur/2 is already visited
				mem[n] = 1 + mem[n >> 1]
				st.pop()
			else:   # If cur/2 is not already visited
				st.append(n >> 1)
		else:   # If cur element is Odd
			if (n+1 in mem) and (n-1 in mem):   # If cur-1 and cur+1 both are already visited
				mem[n] = 1 + min(mem[n + 1], mem[n - 1])
				st.pop()
			else:
				if n-1 not in mem:  # If cur-1 is not already visited
					st.append(n - 1)
				if n+1 not in mem:  # If cur+1 is not already visited
					st.append(n + 1)
	return mem[n]
