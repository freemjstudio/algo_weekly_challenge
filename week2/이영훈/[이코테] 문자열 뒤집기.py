arr = input()

count0 = 0
count1 = 0

if arr[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(len(arr) - 1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

