"Even or Odd"

def eo():
    num = int(input("Enter a Number:"))
    divby = int(input("Give me a numebr to divide by"))
    if num%4 == 0:
        print('Number is a multiple of 4')
    elif num%2 == 0:
        print('Number is Even')
    else:
        print('Number is Odd')

    if num%divby == 0:
        print(num, ' is a multiple of ', divby)
    else:
        print(num,' is not a multiple of ',divby)
