a = int(input("Первое число: "))
b = int(input("Второе число: "))

if a > b:
    print(f'{a} больше {b}')
elif b > a:
    print(f'{b} больше {a}')
else:
    print("Числа равны")