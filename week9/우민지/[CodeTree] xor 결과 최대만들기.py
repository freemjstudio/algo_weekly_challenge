from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cases = list(combinations(arr, m))

# xor 연산
def calc(idx, c, result):
    while True:
        idx += 1
        if idx >= m:
            break
        result = result ^ c[idx]
    return result
answer = 0
for c in cases:
    answer = max(calc(0, c, c[0]), answer)
print(answer)