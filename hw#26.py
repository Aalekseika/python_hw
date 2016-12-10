import random
#1й способ
lst1=[]
for i in range(0,5):
    random_num=random.randint(0,5)
    lst1.append(random_num)
print("First random list:",lst1)
def avr_num1(lst1):
    sum_lst1 = 0
    for i in range(len(lst1)):
        sum_lst1+=lst1[i]
    avr_num1 = sum_lst1 / len(lst1)
    return avr_num1
result1=avr_num1(lst1)

lst2=[]
for n in range(0,5):
    random_num=random.randint(0,5)
    lst2.append(random_num)
print("Second random list:",lst2)
def avr_num2(lst2):
    sum_lst2 = 0
    for n in range(len(lst2)):
        sum_lst2+=lst2[n]
    avr_num2 = sum_lst2 / len(lst2)
    return avr_num2
result2=avr_num2(lst2)

if result1>result2:
    print('The 1st list average number %.2f bigger than the 2nd list average number %.2f' % (result1,result2))
elif result1<result2:
    print('The 1st list average number %.2f less than the 2nd list average number %.2f' % (result1,result2))
else:
    print('The 1st list average number %.2f is equal to the 2nd list average number %.2f' % (result1,result2))


print('========================================')

#2й способ
lst1=[random.randint(0,5)for x in range(0,5)]
print("First random list:",lst1)
lst2=[random.randint(0,5)for y in range(0,5)]
print("Second random list:",lst2)
avr_num1=sum(lst1)/len(lst1)
avr_num2=sum(lst2)/len(lst2)
if avr_num1>avr_num2:
    print('The 1st list average number %.2f bigger than the 2nd list average number %.2f' % (avr_num1,avr_num2))
elif avr_num1<avr_num2:
    print('The 1st list average number %.2f less than the 2nd list average number %.2f' % (avr_num1,avr_num2))
else:
    print('The 1st list average number %.2f is equal to the 2nd list average number %.2f' % (avr_num1,avr_num2))