import time
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


z3()
z3_2()