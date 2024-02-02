import sys

input = sys.stdin.readline

suNo, quizNo = map(int, input().split(' '))

array = list(map(int, input().split(' ')))
prefix_sum = [0]

temp = 0
for i in array:
    temp += i
    prefix_sum.append(temp)

for i in range(0, quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])
