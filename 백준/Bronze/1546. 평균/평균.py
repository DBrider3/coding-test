n = int(input())

array = list(map(int, input().split()))

max_score = max(array)
sum = sum(array)

print(sum / max_score * 100 / n)