def mining(i, m, t):
    for j in range(len(m)):
        if i == 0:
            t += 1
        elif i == 1:
            if m[j] == 'diamond':
                t += 5
            else:
                t += 1
        else:
            if m[j] == 'diamond':
                t += 25
            elif m[j] == 'iron':
                t += 5
            else:
                t += 1
    return t


def solution(picks, minerals):
    answer = 1e9
    q = [[picks[0], picks[1], picks[2], minerals, 0]]

    while q:
        p1, p2, p3, m, t = q.pop(0)
        if p1 > 0:
            if len(m) > 5:
                q.append([p1 - 1, p2, p3, m[5:], mining(0, m[:5], t)])
            else:
                temp = mining(0, m, t)
                if answer > temp:
                    answer = temp
        if p2 > 0:
            if len(m) > 5:
                q.append([p1, p2 - 1, p3, m[5:], mining(1, m[:5], t)])
            else:
                temp = mining(1, m, t)
                if answer > temp:
                    answer = temp
        if p3 > 0:
            if len(m) > 5:
                q.append([p1, p2, p3 - 1, m[5:], mining(2, m[:5], t)])
            else:
                temp = mining(2, m, t)
                if answer > temp:
                    answer = temp
        if p1 == 0 and p2 == 0 and p3 == 0:
            if answer > t:
                answer = t
    return answer