import random

lst=[random.randint(-1,1) for x in range(0,11)]
print("Random list is:",lst)

#1й способ
elem1=0
elem2=0
elem3=0
for i in range(len(lst)):
    if lst[i]==-1:
        elem1+=1
    elif lst[i]==0:
        elem2+=1
    elif lst[i]==1:
        elem3+=1
print('Element -1 meets in the list %d times'% (elem1))
print('Element 0 meets in the list %d times'% (elem2))
print('Element 1 meets in the list %d times'% (elem3))
if elem1>elem2 and elem1>elem3:
    print("Result: element %d meets in the list %d times and it's more often than others two %d and %d" % (
          -1,elem1,0,1))
elif elem2>elem1 and elem2>elem3:
    print("Result: element %d meets in the list %d times and it's more often than others two %d and %d" % (
          0,elem2,-1,1))
elif elem3>elem1 and elem3>elem2:
    print("Result: element %d meets in the list %d times and it's more often than others two %d and %d" % (
          1,elem3,-1,0))

print('===================================================')
#2й способ
elem1=lst.count(-1)
elem2=lst.count(0)
elem3=lst.count(1)
print('Element -1 meets in the list %d times'% (elem1))
print('Element 0 meets in the list %d times'% (elem2))
print('Element 1 meets in the list %d times'% (elem3))
if elem1>elem2 and elem1>elem3:
    print("Result: element %d meets in the list %d times and it's more often than others two %d and %d" % (
          -1,elem1,0,1))
elif elem2>elem1 and elem2>elem3:
    print("Result: element %d meets in the list %d times and it's more often than others two %d and %d" % (
          0,elem2,-1,1))
elif elem3>elem1 and elem3>elem2:
    print("Result: element %d meets in the list %d times and it's more often than others two %d and %d" % (
          1,elem3,-1,0))
