"Guess Game"
#Approach 1 - my approach

import random
def Guess():
    a = random.randint(1,9)
    b = 0
    count = 0
    while a!=b:
        b = int(input("Guess the number:"))
        count += 1
        if a > b:
                print('You have guessed it low')
                
        elif b > a:
                print('You have guessed it high')
        
        else:
                print('You have guessed it correct in ', count, ' attempts')
                if str(input('Do you want to continue? y/n'))== 'y':
                    Guess()
                else:
                    break
                
                
                    
      
