from functools import cmp_to_key


def cmp(x1, x2):
    n1 = int(x1+x2)
    n2 = int(x2+x1)
    if n1 >= n2:
        return -1
    else:
        return 1


K, N = map(int, input().split())
nums = [input() for _ in range(K)]
nums.extend([max(nums, key=int)]*(N-K))
nums.sort(key=cmp_to_key(cmp))
print(''.join(nums))