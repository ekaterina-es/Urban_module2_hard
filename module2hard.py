n = int(input("Введите число (от 3 до 20): "))
result = []

for i in range(1, n):
    for j in range(i + 1, n):
        sum_ = i+j
        if n % sum_ == 0:
            result.append(i)
            result.append(j)

print(f'Нужный пароль для числа "{n}":', *result)








