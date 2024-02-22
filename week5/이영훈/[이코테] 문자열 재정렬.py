string = list(input())

num = 0
alpha = ''

string.sort()

for s in string:
    if s.isdigit():
        num += int(s)
    else:
        alpha += s

print(alpha + str(num))