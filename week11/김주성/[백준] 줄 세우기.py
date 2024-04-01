import sys
input = sys.stdin.readline


def make_tree(node, left, right):
    if left == right:
        tree[node] = 1
        return tree[node]
    mid = (left+right)//2
    s1 = make_tree(node*2, left, mid)
    s2 = make_tree(node*2+1, mid+1, right)
    tree[node] = s1+s2
    return tree[node]


def query(target, start, end, node):
    mid = (start + end) // 2
    tree[node] -= 1
    if start == end:
        return end
    if tree[node*2] >= target:
        return query(target, start, mid, node*2)
    else:
        return query(target-tree[node*2], mid+1, end, node*2+1)


N = int(input())
heights = [int(input()) for _ in range(N)]
small_or_equal = list(map(int, input().split()))

heights.sort()
tree = [0]*(N*4)

make_tree(1, 0, N-1)
answer = [0] * N
for i in range(N-1, -1, -1):
    answer[i] = heights[query(small_or_equal[i]+1, 0, N-1, 1)]

print(*answer, sep='\n')