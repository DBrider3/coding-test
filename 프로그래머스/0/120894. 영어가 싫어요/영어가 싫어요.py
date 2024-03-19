def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for index, value in enumerate(nums):
        numbers = numbers.replace(value, str(index))
        
    return int(numbers)