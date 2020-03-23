"Palindrome"
#Approach 1 - mine yuck

def Strlst1():
    k = str(input("Enter your text:"))
    j=int(len(k))
    c=''
    i=1
    while(i!=j):
        c=c+k[-i]
        i+=1
    c=c+(k[0])
    if c==k:
        print('Palindrome')
    else:
            print('Not Palindrome')
        

#Approach 2 - best***
def Strlst2():
    k = str(input("Enter your text:"))
    c=(k[::-1])
    if c==k:
        print('Palindrome')
    else:
            print('Not Palindrome')
        

#Approach 3 - 2nd best**
def Strlst3():
    k = str((input("Enter your text:")))
    bc=''
    for i in range(len(k)):
        bc=bc+k[len(k)-1-i]
        print(bc)         
    if bc==k:
            print('Palindrome')
    else:
            print('Not Palindrome')
