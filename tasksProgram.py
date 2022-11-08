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
def z7():
    x = int(input("Введите X: "))
    count = 0
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            count += 2
    if float(x ** 0.5) == int(x ** 0.5):
        count += 1

    print(count)

def isSquare(x):
    s = int(sqrt(x))
    return (s * s == x)
def z8():
    n = int(input("Введите N: "))
    m = int(input("Введите M: "))
    a = []
    for i in range(n, m):
        for j in range(i+1, m+1):
            if (isSquare(i*i+j*j)):
                c = sqrt(i*i+j*j)
                if (c <= m):
                    a.append([i, j, int(c)])
    print(a)

def z9_check(l):
    n = len(str(l))
    for i in range(0, n):
        if int(str(l)[i]) == 0 or l % int(str(l)[i]) != 0:
            return False
    return True
def z9():
    n = int(input("Введите N: "))
    m = int(input("Введите M: "))
    a = []
    for i in range(n, m+1):
        if (z9_check(i)):
            a.append(i)
    print(a)
def sumArr(a):
    s = 0
    for i in range(0, len(a)):
        s += a[i]
    return s

def getDivinders(n):
    a = []
    a.append(1)
    i = 2
    while (i*i <= n):
        if (n % i == 0):
            a.append(i)
            if (n/i != i):
                a.append(n/i)
        i += 1
    return a

def z10():
    n = int(input("Введите N: "))
    if (n < 5):
        a = []
        i = 2
        while (n > 0):
            if (sumArr(getDivinders(i)) == i):
                a.append(i)
                n -= 1
            i += 1
        return a
z9()