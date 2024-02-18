import sys

input = sys.stdin.readline

n = int(input())

start_index = 1
end_index = 1
count = 0
sum = 1

while end_index <= n:
    if sum < n:
        end_index += 1
        sum = sum + end_index
    elif sum == n:
        count += 1
        end_index += 1
        sum = sum + end_index
    elif sum > n:
        sum = sum - start_index
        start_index += 1

print(count)
