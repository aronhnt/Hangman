#Hangman Game

import ErrorCheck

def menu():
    running = True
    while running == True:
        print('''
1) Play Game
2) Quit''')
        option = input('Choose An Option: ')
        option = ErrorCheck.errorCheck(option,int,'Choose An Option: ')
        if option == 1:
            print('This Game Is Currently a Work In Progress, Please Follow @aronhnt on github for updates')
        elif option == 2:
            running = False

def main():
    '''For this function, i will need to have:
Number of incorrect attempts - 8
Displaying Empty word e.g. _ _ _ _ _ to user and then adding a letter as guessed
Lists of words - import a file?
Not losing a life if letter guessed twice
allowing only one letter to be entered e.g. aa would not be allowed
other stuff i cant remember'''

menu()
