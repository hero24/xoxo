""" Tic tac toe implementation in python2 """

# The true sign of intelligence is not knowledge but imagination. ~ Albert Einstein

from os import system
from random import randint
# initialise fields to free fields
fields = [" " for x in range(9)]
xo = "o"

def draw_board(lst,xo="x"):
    """
       function for drawing the board.
    """
    counter = 0
    print "%s|"%xo,
    for i in range(3):
        print "%i|"%(i+1),
    print ""
    for i in range(65,68):
        print "%s|"%chr(i),
        for i in range(3):
            print "%s|"%lst[counter],
            counter += 1
        print ""

def take_input(lst,xo="x"):
    """ 
        handle user move against the board
    """
    choice = str(raw_input("Your choice")).upper()
    number_translate = 0
    if choice[0] == "B":
        number_translate = 3
    elif choice[0] == "C":
        number_translate = 6
    choice = number_translate + int(choice[1]) - 1 
    lst[choice] = xo
    
def check_fields(fields):
    winner = _check(fields,0,1,3)
    if not winner or winner == " ":
        winner = _check(fields)
    if not winner or winner == " ":
        winner = _check_cross(fields)
    return winner if winner != " " else False

def _check(fields,index=0,offset=3,vertical_offset=1):
    """ 
       check board for winner.
    """
    if (index + vertical_offset + (offset * 2)) >= len(fields):
        return False
    elif fields[index] == fields[index + (offset * 1)] == fields[index + (offset * 2)]:
        return fields[index]
    elif (index + vertical_offset + (offset * 2)) < len(fields):
        return _check(fields,index + vertical_offset)
    else:
        return False

def _check_cross(fields):
    if fields[0] == fields[4] == fields[8]:
        return fields[0]
    elif fields[2] == fields[4] == fields[6]:
        return fields[2]
    else:
        return False
    
def _computer_turn(fields,xo):
    valid_moves = ["x","o"]
    move = randint(0,len(fields)-1)
    while fields[move] in valid_moves:
        move = randint(0,len(fields)-1)
    fields[move] = valid_moves[valid_moves.index(xo)-1]

def _board_full(fields):
    return " " not in fields
    
    
while True:
    system('cls')
    draw_board(fields,xo)
    winner = check_fields(fields)
    if not winner:
        take_input(fields,xo)
    winner = check_fields(fields)
    system('cls')
    draw_board(fields,xo)
    if not winner:
        _computer_turn(fields,xo)
    elif not winner and _board_full(fields):
        winner = "no one"
    else:
        break
print "%s wins, press any key to exit" % winner
press_any_key  = raw_input()
