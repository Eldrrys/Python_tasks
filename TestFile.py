# Задача 1
def task_1():
    N, d, R = map(int, input('Введите через пробел числа N, d, R: ').split())
    len = (2 * d) + (N * 2 * R)
    return len


# Задача 2
def task_2():
    n = int(input('Введите номер n: '))
    if n <= 10:
        result = n - 1
    elif n <= 190:  # 10 (из пред условия) + 20 * 9 (от 10 до 99), будем начинать отсчет с n-10 для удобства (считаем с 1)
        if (n - 10) % 2 != 0:  # разряд десятков
            result = int((n - 10) / 20) + int((n - 10) / 20 % 2 != 0)
            # В каждой десятке чисел (например 10-19) 20 цифр, поэтому / 20 для отделения разряда десятков (/2 чтобы из 180 цифр почучить 90 чисел и /10 для десятков)
            # Если число в разряде десятков четное, то все ок, если нет, то нужно после целочисленного деления прибавить 1
            # (если номер начинается с 2, то 2 % 2 = 0, ничего не нужно, если с 1, то 1 % 2 = 1 прибавляем единицу)
        else:  # разряд единиц
            result = int((n - 10) / 2 % 10 - int((n - 10) / 2 % 10 != 0)) + 9 * int((n - 10) / 2 % 10 == 0)
            # Аналогично делим на два для перехода к 90 числам, отделяем разряд единиц взятием остатка
            # полученная цифра всегда на 1 больше нужной кроме одного случая с 0. там должно выйти 9, но мы оперируем одноразрядными числами, поэьлму не можеи полоучить 10-1
            # Два последних слагаемых своими проверками на 0 в остатке решают эту проблему, мы не отнимаем 1 и прибавляем 9
    else:
        if (n - 190) % 3 == 2:  # разряд десятков
            result = int((n - 190) % 100 / 30) # просто отделяем вторую цифру числа с оговоркаой на то что в диапазоне 110-119 теперь 30 цифр, поэтому /30, а не /10
        elif (n - 190) % 3 == 1:  # разряд сотен
            result = int((n - 190) / 300) + int((n - 190) % 3 != 0) # Аналогично случаю с двузначными числами с оговоркаой на то что в диапазоне 110-119 теперь 30 цифр
        else:  # разряд единиц
            result = int((n - 190) / 3 % 10) - int((n - 190) / 3 % 10 != 0) + 9 * int((n - 190) / 3 % 10 == 0) # Аналогично случаю с двузначными числами
    return result


# Задача 3
def calculate(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b


def task_3():
    n = int(input('Введите число n: '))
    counter = 0

    for op in range(0, 4):
        x1 = calculate(1, 2, op)
        for op in range(0, 4):
            x2 = calculate(x1, 3, op)
            for op in range(0, 4):
                x3 = calculate(x2, 4, op)
                for op in range(0, 4):
                    x4 = calculate(x3, 5, op)
                    for op in range(0, 4):
                        x5 = calculate(x4, 6, op)
                        if n == x5:
                            counter += 1
    return counter


# Задача 4
def num_counter(N, B, zero):
    # Два случая: текущий разряд 0 или не 0
    # Если 0, то у нас B-1 вариант числа на это место (0 не может быть)
    # Если не 0, то B-1 вариант плюс вариант с 0
    if not N:
        return 1
    if zero:
        return (B - 1) * num_counter(N - 1, B, False)
    else:
        return (B - 1) * num_counter(N - 1, B, False) + num_counter(N - 1, B, True)


def task_4():
   N, B = map(int, input('Введите через пробел числа N, B: ').split())
   return num_counter(N, B, True)


print(task_1())
print(task_2())
print(task_3())
print(task_4())
