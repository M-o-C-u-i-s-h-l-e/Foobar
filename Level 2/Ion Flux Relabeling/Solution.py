def findParent(h, key, leftMax):
    n = (1 << h) - 1
    sub_n = n >> 1
    # key == left child
    if key == sub_n + leftMax:
        return n + leftMax
    # key == right child
    elif key == (sub_n << 1) + leftMax:
        return n + leftMax
    # key in left subtree
    elif key < sub_n + leftMax:
        return findParent(h-1, key, leftMax)
    # key in right subtree
    else:
        return findParent(h-1, key, leftMax+sub_n)

def solution(h, q):
    n = (1 << h) - 1
    res = [findParent(h, i, 0) if i < n else -1 for i in q]
    return res
