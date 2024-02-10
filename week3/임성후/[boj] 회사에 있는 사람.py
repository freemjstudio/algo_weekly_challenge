import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    name_dict = {}
    for _ in range(N):
        name, msg = map(str, input().split())
        name_dict[name] = name_dict.get(name, 0) + 1
    answer = [k for k in name_dict.keys() if name_dict.get(k) % 2 == 1]
    for a in sorted(answer, reverse=True):
        print(a)
