import sys

input = sys.stdin.readline

n = int(input())

start_index = 1
end_index = 1
count = 1
sum = 1

while end_index != n:
    if sum < n:
        end_index += 1
        sum = sum + end_index
    elif sum == n:
        end_index += 1
        sum = sum + end_index
        count += 1
    elif sum > n:
        sum = sum - start_index
        start_index += 1

print(count)
