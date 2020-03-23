"List Overlap"
import random
def List1():
    k = int(input('Enter list size:'))
    a = random.sample(range(1,120),k)
    b = random.sample(range(1,120),k)
    c = set();
    for num in a:
        if num in b:
            c.add(num)
    print(a)
    print(b)
    print(list(c))
    
