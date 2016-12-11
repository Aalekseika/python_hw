#вывести на экран все простые числа от 1 до 100

import math
def primes():
    for i in range(2,101):
        for k in range(2,i):
            if k>int(math.sqrt(i)):
                print(i)
                break
            elif i%2==0:
                break
            elif i%k==0:
                break
        else:
            print(i)
primes()
