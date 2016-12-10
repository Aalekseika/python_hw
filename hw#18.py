#cоздать функцию выводящую на экран случайно сгенерированной 12-значное число и возвращающую
#его наибольшую цифру

import random
def random_12digits_num(n):
    n=random.randint(1e12,1e13)
    return n
result=random_12digits_num(1e12)
def max_num_from_random_12digits_num(n):
    max_num = 0
    while n>0:
        digit=n%10
        if max_num < digit:
            max_num = digit
        n=n//10
    return max_num
result1=max_num_from_random_12digits_num(result)
print("Max number from %d is %d:" % (result, result1))