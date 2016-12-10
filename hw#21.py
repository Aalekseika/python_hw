#вывести все числа от 0 до 1000, которые содержат в себе 1 и 7

for i in range(10,1000):
    _1_found = False
    _7_found = False
    digit = i % 10
    if digit==1:
        _1_found=True
    elif digit==7:
        _7_found = True
    digit = i // 10
    if digit==1:
        _1_found=True
    elif digit==7:
        _7_found = True
    digit = i % 100//10
    if digit == 1:
        _1_found = True
    elif digit == 7:
        _7_found = True
    digit = i//100
    if digit == 1:
        _1_found = True
    elif digit == 7:
        _7_found = True
    if _1_found == True and _7_found == True:
        print(i)