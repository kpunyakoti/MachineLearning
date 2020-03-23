#Blank#

import random

def LE():

    a = random.sample(range(1,100),10)
    b = Lst_Ends(a)
    print(a)
    print(b)
    

def Lst_Ends(a_list):
    return [a_list[0],a_list[len(a_list)-1]]



