#global variables
#board
board=[" "," "," ",
       " "," "," ",
       " "," "," "]
# is game over or not
game_not_over=True

winner=[None]
#display board
def display_board():
    print("-|1|--|2|--|3|-")
    print("[ "+board[0]+" ][ "+board[1]+" ][ "+board[2]+" ]")
    print("-|4|--|5|--|6|-")
    print("[ " + board[3] + " ][ " + board[4] + " ][ " + board[5] + " ]")
    print("-|7|--|8|--|9|-")
    print("[ " + board[6] + " ][ " + board[7] + " ][ " + board[8] + " ]")
    print("-|-|--|-|--|-|-")
#player how plays first it is 0
player="O"

# main method
def play_game(player,game_not_over):
    display_board()
    while game_not_over:
        handle_turn(player)
        player=flip_palyer(player)
        game_not_over=check_if_over(game_not_over)
        # print(game_not_over)




def handle_turn(player):
    position=input("Choose a position to put your peace:")
    if((not validation_for_input_number(position)) ):
        print("position wrong enter valid position")
        return


    position=int(position)-1
    if(board[position]!=' '):
        print('postion was already taken ')
        return
    board[position]=player
    display_board()
#chewck if win
def check_if_win(game_is_over):
    check1=check_if_equal(0,1,2)
    check2 = check_if_equal(3, 4, 5)
    check3 = check_if_equal(6, 7, 8)
    check4 = check_if_equal(0, 3, 6)
    check5 = check_if_equal(1, 4, 7)
    check6 = check_if_equal(2, 5, 8)
    check7 = check_if_equal(0, 4, 8)
    check8 =check_if_equal(6,4,2)

    if(     check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8

    ):


        game_not_over=False
    else:
        game_not_over=True


    return game_not_over

def check_if_equal(a,b,c):
    if(board[a]==board[b] and board[b]==board[c] and board[a]!=" "):
        print(' the winner is ' + board[a])
    return board[a]==board[b] and board[b]==board[c] and board[a]!=" "

#check where we tie
def check_if_tie(game_not_over):
    if(board[0]!=" " and  board[1]!=" " and board[2]!=" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and board[7]!=" " and board[8]!=" "):
        print(board[0])
        game_not_over=False
        print("The game was a draw")
    return game_not_over
#flip the players
def flip_palyer(player):
    if(player=="O"):
        player="X"
    else:
        player="O"

    return player
#check if the game is over
def check_if_over(game_not_over):
    if(not (check_if_tie(game_not_over)) or not (check_if_win(game_not_over))):
        game_not_over=False
    else:
        game_not_over=True

    return game_not_over


def validation_for_input_number(num):
    if (num=='1' or num=='2' or num =='3' or num=='4' or num=='5' or num=='6' or num=='7' or num=='8'or num=='9' ):
        return True
    else :
        return False

#start very thing
play_game(player,game_not_over)
print(" thank you for playing")
#play game
#handle turn
#check win
#check rows
#check columns
#check diaganal
#check tie
#flip player
