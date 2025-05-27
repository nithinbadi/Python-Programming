'''
TIC TAC TOE
- 2 players should be able to play the game on the same computer.
- the board should be printed out every time a player makes a move
- You should be able to accept input of the player position and then place a symbol on the board.

Numpad that matches numbers to the grid on a tic tac toe board - 



Player one is X
Player two is O

'''

import os

board = ['1','2','3','4','5','6','7','8','9']

def print_board(board = board):
    '''
    Functionality - prints the board as   
    
   
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    

        board: a list of lists that represents the tic tac toe board.
    '''

    os.system('cls')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('\n---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('\n---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    

def check_position(pos, board):
    

    if pos not in '123456789':
        return False
    elif board[int(pos)-1] == 'X' or board[int(pos)-1] == 'O':
        print("Invalid position")
        return False
    else:
        return True  
    

def check_win(board,player):
    
    # Check row win

    # Row check
    if (board[0] == player and board[1] == player and board[2] == player) or (board[3] == player and board[4] == player and board[5] == player) or (board[6] == player and board[7] == player and board[8] == player):
        print('Player {} wins!'.format(player))
        return True
    
    # Column check
    if (board[0] == player and board[3] == player and board[6] == player) or (board[1] == player and board[4] == player and board[7] == player) or (board[2] == player and board[5] == player and board[8] == player):
        print('Player {} wins!'.format(player))
    
    # Diaganol check
    if (board[0] == player and board[4] == player and board[8] == player) or (board[2] == player and board[4] == player and board[6] == player):
        return True
    
    
    # If none of the conditions no player has won and the game continues
    return False

def check_draw(board):
    sum=0
    for pos in board:
        if pos in '123456789':
            return False
        else:
            sum = sum + 1 
    if sum == 9:
        return True

def update_board(board,pos, player):
    if check_position(pos, board):

        # Update board if position is valid
        board[int(pos)-1] = player
        return board
    else:
        return board

# Game begins
print_board(board)
print('TIC TAC TOE GAME BEGINS\n')


# print(check_draw(['X','O','X','O','O','X','O','X','O']))
# Player 'X' is n=0 and Player 'O' is n=1
n=0
while True:
    player = 'X' if n%2 == 0 else'O'
    
    # Player input between 1 and 9. pos variable applies to Player X or Player O
    pos = input("Choose positions between 1-9: \n")

    # Check position
    if not check_position(pos,board):
        print("Enter a valid position: \n")
        continue
    else:
        # Update the board
        board = update_board(board = board, pos = pos, player = player )
   
        # Check draw
        if check_draw(board):
            print_board(board)
            print('The game has ended in a Draw\n')
            break
        # Check for winners
        elif check_win(board, player='X') or check_win(board, player='O'):
            print_board(board)
            print(f'{player} Won\n') 
            break   
        # Change player and continue the game
        else:
            n=n+1
            print_board(board)
    
    
    


