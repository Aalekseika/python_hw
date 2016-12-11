#Условие:
#программа выбирает случайное число от 1 до 10 и предлагает поль-лю его угадать
#поль-ль вводит число, а программа его проверяет
#если поль-ль не угадал, программа говорит больше или меньше и просит опять угадать
#и так до тех пор пока поль-ль не угадает

import random
def random_num(n):
    n=random.randint(1,11)
    return n
result=random_num(10)
print("Random number is:",result)
s=int(input("Make your choice:"))
while s!=result:
    if s>result:
        print("The number is bigger than random number",result)
        s = int(input("Please, try again:"))
    elif s<result:
        print("The number is less than random number",result)
        s = int(input("Please, try again:"))
print("Congrats! %d is right choice" % s)
