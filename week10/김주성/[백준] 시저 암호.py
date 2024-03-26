def get_pattern(pattern):
    pattern_length = len(pattern)
    pattern_lps = [0] * pattern_length
    idx = 0
    for k in range(1, pattern_length):
        while idx > 0 and pattern[k] != pattern[idx]:
            idx = pattern_lps[idx-1]
        if pattern[k] == pattern[idx]:
            idx += 1
            pattern_lps[k] = idx
    return pattern_lps


def kmp(string, pattern, pattern_lps):
    idx = 0
    count = 0
    for k in range(len(string)):
        while idx > 0 and string[k] != pattern[idx]:
            idx = pattern_lps[idx-1]
        if string[k] == pattern[idx]:
            if idx == len(pattern)-1:
                count += 1
                idx = pattern_lps[idx]
            else:
                idx += 1
    return count


t = int(input())

for _ in range(t):
    A = list(input())
    W = list(input())
    S = list(input())

    key = []

    dic = {}
    for i in range(len(A)):
        dic[A[i]] = i

    for i in range(len(W)):
        W[i] = dic[W[i]]

    for i in range(len(S)):
        S[i] = dic[S[i]]

    lps = get_pattern(W)
    for i in range(len(A)):
        temp = [(W[j]+i) % len(A) for j in range(len(W))]
        if kmp(S, temp, lps) == 1:
            key.append(i)

    if len(key) == 0:
        print('no solution')
    elif len(key) == 1:
        print(f'unique: {key[0]}')
    else:
        print('ambiguous:', end=' ')
        print(*key, sep=' ')