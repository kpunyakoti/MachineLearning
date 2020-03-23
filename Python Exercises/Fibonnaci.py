#Blank#

def Fib():
    n = int(input('Enter number of Fibonacci numbers you want: '))

    a = [1]
    b = 1
    c = 2
    while (c<=n):
        if c==2:
            b=1
        else:
            b=(a[-1])+(a[-2])
        a.append(b)
        c =c+1
    print(a)
