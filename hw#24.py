#Условие:
#написать функцию для поиска разницы между суммой всех четных и нечетных чисел списка
#от суммы четных чисел вычесть сумму нечетных чисел в списке


def even_odd_difference(lst):
    sum_lst1=0
    sum_lst2=0
    for i in range(len(lst)):
        number=lst[i]%2==0
        if number==True:
            sum_lst1+=lst[i]
        elif number==False:
            sum_lst2+=lst[i]
    difference=sum_lst1-sum_lst2
    return difference
result=even_odd_difference([1,2,3,4,5,6,7,8,9,10])
print(result)
