"Rock Paper Scissors"

def rps():

    while True:
        game_dict = {'rock':1, 'scissors':2, 'paper':3}
        a = str(input("Player 1 - Enter your input:"))
        b = str(input("Player 2 - Enter your input:"))
        c = game_dict.get(a)
        d = game_dict.get(b)
        diff = c - d
           
        if diff in [-1,2]:
            print('Congratualtions Player 1!! You Win!!')
            if str(input('do you want to continue? y/n'))=='y':
                continue
            else:
                print('Game Over')
                break
        elif diff in [-2,1]:
            print('Congratualtions Player 2!! You Win!!')
            if str(input('do you want to continue? y/n'))=='y':
                continue
            else:
                print('Game Over')
                break
        else:
            print('Game draw. Please continue')
            print('')
            

        
        
            
        
