from random import randint
from registering import Register
from  see_the_leader_board import See
class Game:
    def __init__(self,username):
        num = int(randint(0,100))
        a = 1
        Notdone = True
        while Notdone:
            i = input('guess the number:')
            if int(i) >num:
                a += 1
                print('lower')
            elif int(i) < num:
                a += 1
                print('higher')
            elif int(i) == num:
                Register(username,a)
                Notdone = False
Game('sas')
#hello me!