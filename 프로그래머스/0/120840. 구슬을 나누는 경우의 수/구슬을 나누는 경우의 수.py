def my_factorial(n):
    if n > 1:
        return n * my_factorial(n - 1)
    else:
        return 1

def solution(balls, share):
    return my_factorial(balls) // (my_factorial(balls - share) * my_factorial(share))
