import sys

input = sys.stdin.readline


def get_pattern():
    idx = 0
    for i in range(1, len(text)):
        while idx > 0 and text[i] != text[idx]:
            idx = lps[idx-1]
        if text[i] == text[idx]:
            idx += 1
            lps[i] = idx

while True:
    text = input().rstrip()
    if text == '.':
        break
    text_length = len(text)
    lps = [0] * text_length
    get_pattern()

    pattern_length = text_length-lps[-1]
    if text_length % pattern_length == 0:
        print(text_length//pattern_length)
    else:
        print(1)