#Blank#

def nodupes_1(y):
    x= []
    for i in y:
        if i not in x:
            x.append(i)
    return x

def nodupes_2(a_list):  
    x = list(set(a_list))
    return x

a = [1,2,3,4,5,4,8,7,2,12,13,12,14,19,22,4,21,20,20]
print(a)
b = nodupes_1(a)
print(b)
c = nodupes_2(a)
print(c)

