my_list = [0] * 4
check_list = [0] * 4
check_secret = 0

def my_add(d):
    global my_list, check_list, check_secret

    if d == 'A':
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            check_secret += 1
    elif d == 'C':
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            check_secret += 1
    elif d == 'G':
        my_list[2] += 1
        if my_list[2] == check_list[2]:
            check_secret += 1
    elif d == 'T':
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            check_secret += 1


def my_remove(d):
    global my_list, check_list, check_secret

    if d == 'A':
        if my_list[0] == check_list[0]:
            check_secret -= 1
        my_list[0] -= 1
    elif d == 'C':
        if my_list[1] == check_list[1]:
            check_secret -= 1
        my_list[1] -= 1
    elif d == 'G':
        if my_list[2] == check_list[2]:
            check_secret -= 1
        my_list[2] -= 1
    elif d == 'T':
        if my_list[3] == check_list[3]:
            check_secret -= 1
        my_list[3] -= 1


s, p = map(int, input().split())
dna = list(input())
check_list = list(map(int, input().split()))
count = 0

# 0 일 경우 이미 무조건 만족했을때니 체크항목 ++
for i in range(4):
    if check_list[i] == 0:
        check_secret += 1

# 초기 p개수 셋팅
for i in range(p):
    my_add(dna[i])

# 체크 항목이 모두 충족할 시 count ++
if check_secret == 4:
    count += 1

# 슬라이딩 윈도우
for i in range(p, s):
    j = i - p
    my_add(dna[i])
    my_remove(dna[j])
    if check_secret == 4:
        count += 1

print(count)
