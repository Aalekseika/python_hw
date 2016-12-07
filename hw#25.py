# 1й способ
lst=[]
for i in range(1,100):
    if i%2!=0:
        lst.append(i)
print("The list from odd numbers from %d to %d is: %s" % (1,99,lst))

import random
lst1=[]
while len(lst1) != len(lst):
    random_num=random.choice(lst)
    if random_num not in lst1:
        lst1.append(random_num)
print("Reshuffled list from odd numbers from %d to %d is: %s" % (1,99,lst1))

print("=================================================")
# 2й способ
list=[x for x in range(1,100) if x%2!=0]
print("The list from odd numbers from %d to %d is: %s" % (1,99,list))

list2=list
random.shuffle(list2)
print("Reshuffled list from odd numbers from %d to %d is: %s" % (1,99,list2))