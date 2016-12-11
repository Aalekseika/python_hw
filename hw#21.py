#вывести все числа от 0 до 1000, которые содержат в себе 1 и 7

for i in range(10,1000):
    num = i
    _1_found = False
    _7_found = False

    while (i>0):
        digit = i % 10
        i = i // 10
        if digit == 1:
            _1_found = True
        elif digit == 7:
            _7_found = True
    if _1_found == True and _7_found == True:
        print(num)
