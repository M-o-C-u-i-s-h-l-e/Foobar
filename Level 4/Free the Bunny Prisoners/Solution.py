from itertools import combinations

def solution(num_buns, num_required):
	res = [[] for i in range(num_buns)]
	# If not enough bunnies are present
	if num_buns < num_required:
		return res
	# No. of times each key is required
	times = num_buns - num_required + 1
	# Generate all combinations of required size
	ls = list(range(num_buns))
	groups = combinations(ls, times)
	# Distribute keys to bunny groups using the generated combinations
	for cur_num, group in enumerate(groups):
		for i in group:
			res[i].append(cur_num)
	return res
