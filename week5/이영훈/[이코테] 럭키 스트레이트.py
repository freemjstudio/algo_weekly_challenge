n = input()

criterion = len(n) // 2

left = n[:criterion]
right = n[criterion:]

left_sum, right_sum = 0, 0

for num in left:
    left_sum += int(num)

for num in right:
    right_sum += int(num)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')