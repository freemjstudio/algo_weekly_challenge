S, K = input().split()
K = int(K)

lps = [0] * len(S)
idx = 0

for i in range(1, len(S)):
    while idx > 0 and S[i] != S[idx]:
        idx = lps[idx-1]
    if S[i] == S[idx]:
        idx += 1
        lps[i] = idx

print((len(S)-lps[-1])*(K-1)+len(S))