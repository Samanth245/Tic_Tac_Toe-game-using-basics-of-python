import random

def space_check(board,position):

    return board[position] == ' '

def position_check(board):
    
    position = 0

    while position not in list(range(1,10)) or not space_check(board,position):
        position = int(input('Please choose positon {1,9} : '))

    return position    

def place_marker(board,marker,position):
    
    board[position] = marker

def choose_first():
    
    first = random.randint(0,1)

    if first == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def display_board(board):
    print('\n'*100)
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('_________\n')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('_________\n')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False

    return True 

def player_marker():
    marker = ' '

    while marker not in ['X' , 'O']:
        marker = input('Player marker {X/O} : ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def win_check(board,marker):

    return (board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or (board[7] == board[8] == board[9] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker) or (board[1] == board[5] == board[9] == marker) or (board[3] == board[5] == board[7] == marker)

def replay():

    Next_Game = input('Want to play again? (Y/N) : ').upper()

    return Next_Game == 'Y' 

#Start 
print('Welcome to Tic_Tac_Toe!')

while True:
    #Define Player Board
    player_board = [' ']*10
    
    #Display Player Board
    display_board(player_board)

    #Choose marker either 'X' or 'O'
    player1_marker, player2_marker = player_marker()

    #Choose who start first randomly 
    turn = choose_first()

    print(turn + ' will go first')

    Ready = input('Ready to Start? (Y/N) : ').upper()

    if Ready == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player 1 gameplay
        if turn == 'Player 1':
            #Initially Display Board
            display_board(player_board)

            #Choose Position
            position = position_check(player_board)

            #place marker in that position 
            place_marker(player_board,player1_marker,position)

            #check win
            if win_check(player_board,player1_marker):
                display_board(player_board)
                print('Player 1 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(player_board):
                    display_board(player_board)
                    print('TIE GAME!!!')
                    game_on = False
                else:
                    turn = 'Player 2'

        #Player 2 gameplay
        if turn == 'Player 2':
            #Initially Display Board
            display_board(player_board)

            #Choose Position
            position = position_check(player_board)

            #place marker in that position 
            place_marker(player_board,player2_marker,position)

            #check win
            if win_check(player_board,player2_marker):
                display_board(player_board)
                print('Player 2 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(player_board):
                    display_board(player_board)
                    print('TIE GAME!!!')
                    game_on = False
                else:
                    turn = 'Player 1'  

    if not replay():
        break                       