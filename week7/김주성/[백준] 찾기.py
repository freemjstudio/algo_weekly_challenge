T = input().rstrip()
P = input().rstrip()

pattern_length = len(P)
lps = [0] * pattern_length

idx = 0
for i in range(1, pattern_length):
    while idx > 0 and P[i] != P[idx]:
        idx = lps[idx-1]

    if P[i] == P[idx]:
        idx += 1
        lps[i] = idx

answer = []

idx = 0
for i, t in enumerate(T):
    while idx > 0 and T[i] != P[idx]:
        idx = lps[idx-1]
    if T[i] == P[idx]:
        if idx == pattern_length-1:
            answer.append(i-idx+1)
            idx = lps[idx]
        else:
            idx += 1

print(len(answer))
print(' '.join([str(i) for i in answer]))