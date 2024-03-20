import sys
input = sys.stdin.readline
A = input().rstrip()
B = (input().rstrip()*2)[:-1]

answer = 0
text_length = len(A)
lps = [0] * text_length

idx = 0
for i in range(1, text_length):
    while idx > 0 and A[i] != A[idx]:
        idx = lps[idx-1]
    if A[i] == A[idx]:
        idx += 1
        lps[i] = idx

idx = 0
for i in range(text_length*2-1):
    while idx > 0 and B[i] != A[idx]:
        idx = lps[idx-1]
    if B[i] == A[idx]:
        if idx == text_length-1:
            answer += 1
            idx = lps[idx]
        else:
            idx += 1

print(answer)