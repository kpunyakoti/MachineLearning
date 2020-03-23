"List Of Tens"

def LT():
    a = [1,2,3,4,5,1,13,12,15,18,10,21,46,53,72,27,38,86,92]
    ref = int(input('Enter a Number:'))
    list1 = []
    list2 = []
    for output in a:
        if output < ref:
            list1.append(output)
    for output in a:
        if output > ref:
            list2.append(output)
    print('Numbers lesser than ',ref,':',list1)
    print('Numbers greater than ',ref,':',list2)
    
            
    
