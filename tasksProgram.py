import time

from math import sqrt
from memory_profiler import profile

@profile
def z1():
    time_start = time.perf_counter()
    a, b, c = 1, 2, 3
    b, c, a = c, a, b
    print(a, b, c)
    time_elapsed = (time.perf_counter() - time_start)
    print("%5.1f secs" % (time_elapsed))

def is_num(n):
    b = True
    try:
        float(n)
    except ValueError:
        print("Это не число")
        b = False
    return b

def z2():
    sum = 0
    n = input("Введите сколько чисел вы хотите суммировать: ")
    if is_num(n):
        n = int(n)
    s = input("Введите " + str(int(n)) + " чисел через пробел: ").split()
    if (len(s) != n):
        print("Давайте заново")
        z2()
        return
    for n in s:
        if is_num(n):
            sum += float(n)
        else:
            print("Давайте заново")
            z2()
            return
    print("Сумма "+ str(sum))

@profile
def z3():
    time_start = time.perf_counter()
    x = int(input("Введите X: "))
    print(x ** 5)
    time_elapsed = (time.perf_counter() - time_start)
    print("%5.1f secs" % (time_elapsed))

@profile
def z3_2():
    time_start = time.perf_counter()
    x = int(input("Введите X: "))
    print(x*x*x*x*x)
    time_elapsed = (time.perf_counter() - time_start)
    print("%5.1f secs" % (time_elapsed))

def z4():
    n = int(input("Введите число: "))
    if sqrt(5 * (n ** 2) - 4) % 1 == 0 or sqrt(5 * (n ** 2) + 4) % 1 == 0:
        print("Из ряда фибоначи")
    else:
        print("Не из ряда фибоначи")

def z5_1():
    n = int(input("Введите номер месяца: "))
    if (n < 3 or n == 12):
        print("Зима")
    elif (2 < n <= 5):
        print("Весна")
    elif (5 < n <= 8):
        print("Лето")
    else:
        print("Осень")
def z5_2():
    n = int(input("Введите номер месяца: "))
    d = {
        "Зима": (12, 1, 2),
        "Весна": (3, 4, 5),
        "Лето": (6, 7, 8),
        "Осень": (9, 10, 11)
    }
    for key in d:
        if (n in d[key]):
            print(key)
def z6():
    x = int(input("Введите X: "))
    s1, s2 = 0, 0
    if (x % 2 == 0):
        s1 = (1 + x-1) * (x // 2) / 2
        s2 = (2 + x) * (x // 2) / 2
    else:
        s1 = (1 + x) * (x // 2) / 2
        s2 = (2 + x-1) * (x // 2) / 2
    print(f"Сумма всех нечетных: {s1}")
    print(f"Сумма всех четных: {s2}")
z6()