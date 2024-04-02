n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
prefix_sum = [0] * (n+1)
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
#print(prefix_sum)
for i in range(k, n):
    diff = prefix_sum[i] - prefix_sum[i-k]
    answer = max(answer, diff)

print(answer)