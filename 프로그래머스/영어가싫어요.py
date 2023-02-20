def solution(numbers):
    answer = 0
    num_s=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i, num in enumerate(num_s):
        numbers=numbers.replace(num,str(i))
        
    return int(numbers)