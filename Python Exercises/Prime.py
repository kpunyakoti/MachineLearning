#Prime Number#


def Prime():
    a = int(input('Enter a Number:'))
    if a <0 or a in (0,1): print('Not a Prime Number')
    elif a==2: print('Prime Number')
    else:
        b = 2
        while (b !=a):
            if a%b == 0:
                print('Not a prime number')
                break
            elif (a-b==1):
                print('Prime Number')
                break
            else: b+=1
        
    
