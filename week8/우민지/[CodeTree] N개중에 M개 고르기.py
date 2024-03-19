n = 3
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

# cur_num 위치에 0 또는 1을 선택하는 함수
def choose(cur_num):
    if cur_num == n+1:
        print_answer()
        return
    answer.append(0)
    choose(cur_num+1)
    answer.pop()

    answer.append(1)
    choose(cur_num+1)
    answer.pop()

choose(1)