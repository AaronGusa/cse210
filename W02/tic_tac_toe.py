'''
Aaron Gusa
CSE 210 - Programming with Classes
Brother Richards
W02

'''


def main():
    # Initial variables
    init_values = [1,2,3,4,5,6,7,8,9]
    i = -1 
    win_condition = False
    draw = False
    
    # Main game loop
    while win_condition == False:
        if draw == False:

            i = i + 1 
            print(f'\nTurn: {i}')
            xo = x_or_o(i)
            tic_tac_maker(init_values)
            selection(init_values, xo)

            win_condition = win_check(init_values, i)
        else:
            win_condition = True
            draw = True

    winnerwinnerchickendinner(xo, init_values, win_condition, draw)
    

# Functions
def tic_tac_maker(grid):
    
    print(f'''
     {grid[0]} | {grid[1]} | {grid[2]}
    ---+---+---
     {grid[3]} | {grid[4]} | {grid[5]}
    ---+---+---
     {grid[6]} | {grid[7]} | {grid[8]}
    ''')

def x_or_o(turn):
    
    player = ""
    if int(turn) % 2 == 0:
        player = "X"
    else:
        player = "O"
    
    return player

def selection(values, xo):
    choice = int(input(f"{xo}'s turn to choose a square (1-9): "))
    values[choice - 1] = xo

def win_check(values, turn_limit):
    if values[0] == "X" and values[1] == "X" and values[2] == "X":
        win_check = True
    elif values[0] == "X" and values[4] == "X" and values[8] == "X":
        win_check = True
    elif values[0] == "X" and values[3] == "X" and values[6] == "X":
        win_check = True
    elif values[1] == "X" and values[4] == "X" and values[7] == "X":
        win_check = True
    elif values[2] == "X" and values[5] == "X" and values[8] == "X":
        win_check = True
    elif values[2] == "X" and values[4] == "X" and values[6] == "X":
        win_check = True
    elif values[3] == "X" and values[4] == "X" and values[5] == "X":
        win_check = True
    elif values[6] == "X" and values[7] == "X" and values[8] == "X":
        win_check = True
    elif values[0] == "O" and values[1] == "O" and values[2] == "O":
        win_check = True
    elif values[0] == "O" and values[4] == "O" and values[8] == "O":
        win_check = True
    elif values[0] == "O" and values[3] == "O" and values[6] == "O":
        win_check = True
    elif values[1] == "O" and values[4] == "O" and values[7] == "O":
        win_check = True
    elif values[2] == "O" and values[5] == "O" and values[8] == "O":
        win_check = True
    elif values[2] == "O" and values[4] == "O" and values[6] == "O":
        win_check = True
    elif values[3] == "O" and values[4] == "O" and values[5] == "O":
        win_check = True
    elif values[6] == "O" and values[7] == "O" and values[8] == "O":
        win_check = True
    elif turn_limit >= 8:
        win_check = "draw"
    else:
        win_check = False
    
    return win_check

def winnerwinnerchickendinner(xo, values, win, draw):
    if win == True and draw == False:
        print()
        print(' ' * 6 + 'WINNER!')
        tic_tac_maker(values)
        print(f"Congratulations to {xo}!\n")
    else:
        print()
        print(' ' * 7 + 'DRAW!')
        tic_tac_maker(values)
        
# Run main
if __name__ == "__main__":
    main()