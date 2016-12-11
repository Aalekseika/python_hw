#Условие:
#написать функцию которая расчитывает сумму числовых кодов для всех символов из диапазона от А до D.

A=ord('A')
B=ord('B')
C=ord('C')
D=ord('D')
def sum_numbers(A,D):
    accumulator = 0
    for i in range(A,D+1):
        if A<=i<=D:
            accumulator+=i
    return accumulator
result=sum_numbers(A,D)
print("Sum of number codes Unicodes's symbols from %s to %s is equal %d:" % ('A','D',result))
