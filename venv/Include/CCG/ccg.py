computer_score=int(0)
user_score=int(0)
import random
name=input('Enter your name to play')

def play_again():
    print('Do you want to play again '.upper())
    tryagain=input('yes=1/no=0').lower()
    if tryagain==yes:
        return 1
    else:
        return 0


# comparing function
def  compare_input(user_input,coomputer):
    if user_input==coomputer:

        return True
    else:

        return False



lst=['RED','BLUE','GREEN','YELLOW ','BLACK ']
tryagain=1
while tryagain!=0 :

    user_choice= int(input('Enter a Number to see if the you have the same color is computer\n'
              'RED = 1\n'
              'BLUE = 2\n'
              'GREEN = 3\n'
              'YELLOW = 4\n'
              'BLACK = 5\n'))
   


    computer_choice=random.randrange(1,6)

    bool_check=compare_input(user_choice,computer_choice)
    if bool_check:
        user_score+=1
        print(name.upper() , ' YOU WON: YOUR CHOICE WAS', lst[user_choice-1] ,'\nAND '
                    'THAT OF THE COMPUTER IS',lst[computer_choice-1] ,'\n' 
                    'User Score:',user_score,'\nComputer: ', computer_score)

        print('Do you want to play again '.upper())
        tryagain = int(input('yes=1/no=0'))
    else:
        computer_score+=1
        print(name.upper(), ' YOU LOST: YOUR CHOICE WAS', lst[user_choice - 1], '\nAND '
                    'THAT OF THE COMPUTER IS', lst[computer_choice - 1], '\n'
                 'User Score:', user_score, '\nComputer: ', computer_score)

        print('Do you want to play again '.upper())
        tryagain = int(input('yes=1/no=0'))




