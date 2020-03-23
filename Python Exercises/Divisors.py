"Divisors"

def Div():
    ref = int(input('Enter a Number:'))
    x = range(2,ref)
    divisors = []
    for divisor in x:
        if ref%divisor == 0:
            divisors.append(divisor)
    print('Divisors of ',ref,':',divisors)

    
            
    
