#написать функцию для поиска среднего арифметического всех элементов списка

def avr_num(lst):
    sum_lst = 0
    for i in range(len(lst)):
        sum_lst+=lst[i]
    average = sum_lst/len(lst)
    return average
result=avr_num([1,2,3,4,5,6,7,8,9,10])
print(result)
