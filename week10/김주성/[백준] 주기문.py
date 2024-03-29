string = input()
lps = [0] * len(string)

idx = 0
for i in range(1, len(string)):
    while idx > 0 and string[i] != string[idx]:
        idx = lps[idx-1]
    if string[i] == string[idx]:
        idx += 1
        lps[i] = idx

for i in range(len(string)):
    string_length = i+1-lps[i]
    if (i+1)%string_length == 0 and (i+1)//string_length >= 2:
        print(i+1,(i+1)//string_length)
