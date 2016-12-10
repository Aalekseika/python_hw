n=int(input('The number is:'))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

result=factorial(n)
print("Factorial from %d is equal:" % n, result)