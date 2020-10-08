pos = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def valid(x, y, r, c):
	return (x >= 0 and x < r and y >= 0 and y < c)

def solution(maze):
	r, c = len(maze), len(maze[0])
	visited = set()
	Count = 1
	queue = [[0, 0, 0]]
	while (len(queue)):
		sz = len(queue)
		for i in range(sz):
			x, y, breaked = queue.pop(0)
			if x == r-1 and y == c-1:
				return Count
			elif (x, y, breaked) in visited:
				continue
			elif breaked & maze[x][y]:
				continue
			visited.add((x, y, breaked | maze[x][y]))
			for j in range(4):
				if valid(x+pos[j][0], y+pos[j][1], r, c):
					queue.append([x+pos[j][0], y+pos[j][1], breaked | maze[x][y]])
		Count += 1
	return Count
