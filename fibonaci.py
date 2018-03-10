import pyperclip

# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a, b = b, a+b
#     return a

def fib(n):
    if n <= 0:
        if n % 2 == 0:
            return -fib(-n)
        else:
            return fib(-n)
    if n == 1 or n ==1:
        return 1
    a, b = 1,1
    for i in range (n-1):
        a, b = b, a+b
    return a

while True:
    a = int(raw_input())
    # if a < 0:
    #     a = a*(-1)
    #     b = fib(a)
    #     b = b * pow(-1, a-1)
    #     print b
    #     pyperclip.copy(str(b))

    # else:
    b = str(fib(a))
    pyperclip.copy(b)
    print b



