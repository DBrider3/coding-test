import sys

input = sys.stdin.readline

# 재료의 개수
n = int(input())

# 갑옷을 만드는데 필요한 수
m = int(input())

materials = list(map(int, input().split(' ')))
materials.sort()

start = 0
end = len(materials) - 1

count = 0

while start < end:
    sum = materials[start] + materials[end]
    if sum < m:
        start += 1
    elif sum > m:
        end -= 1
    else:
        count += 1
        end -= 1

print(count)










