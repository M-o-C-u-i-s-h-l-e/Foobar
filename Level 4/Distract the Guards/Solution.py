# Returns true if a matching for vertex u is possible
def bpm(graph, u, matchR, seen, n):
    for v in range(n):
        if graph[u][v] and seen[v] == False:
            seen[v] = True
            if matchR[v] < 0 or bpm(graph, matchR[v], matchR, seen, n):
                matchR[v] = u
                return True
    return False

# Returns maximum number of matching
def maxBPM(graph, n):
    matchR = [-1] * n
    res = 0
    for i in range(n):
        seen = [False] * n
        if bpm(graph, i, matchR, seen, n):
            res += 1
    return res

# To find gcd of a and b
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# To find if a, b forms a loop or not
def ifLoop(a, b):
    if a == b:
        return 0
    if (a + b) % 2 == 1:
        return 1
    GCD = gcd(a, b)
    a, b = a // GCD, b // GCD
    if a < b:
        a, b = b, a
    return ifLoop(a - b, b << 1)

# Convert list into a graph
def createGraph(ls, n):
    graph = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            graph[i][j] = ifLoop(ls[i], ls[j])
            graph[j][i] = graph[i][j]
    return graph

def solution(banana_list):
    graph = createGraph(banana_list, len(banana_list))
    return len(banana_list) - ((maxBPM(graph, len(banana_list)) >> 1) << 1)
