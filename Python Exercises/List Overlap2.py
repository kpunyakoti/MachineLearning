"Palindrome"
#Approach 1 - mine yuck

import random
def LstOvrlp():
    a = random.sample(range(1,100),12)
    b = random.sample(range(1,100),10)
    
    c = set()
    for k in a:
        if k in b:
            c.add(k)

    print(a)
    print(b)
    print(c)
    
    
