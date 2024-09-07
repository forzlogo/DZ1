a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if b == 0:
    pass
else:
    if a % b == 0:
        print("Делится без остатка")
    else:
        print("Не делится без остатка")