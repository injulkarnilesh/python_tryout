
UNOCCUPIED = " "
PLAYER_X = "X"
PLAYER_O = "O"

board = [UNOCCUPIED for place in range(9)]

def print_board_line(*places) :
    print("| {} | {} | {} |".format(*places))
    
def print_board() :
    print_board_line(board[0], board[1], board[2])
    print_board_line(board[3], board[4], board[5])
    print_board_line(board[6], board[7], board[8])

def next_player(current_player) :
    if current_player == PLAYER_X :
        return PLAYER_O
    else :
        return PLAYER_X

def is_valid_place(index) :
    return index in range(9) and board[index] == UNOCCUPIED

def are_same_places(places, player) :
    same = True
    for place in places :
        if board[place] != player :
            same = False
            break
    return same    

def has_won(player) :
    return are_same_places([0, 1, 2], player = player) or \
           are_same_places([3, 4, 5], player =  player) or \
           are_same_places([6, 7, 8], player = player) or \
           are_same_places([0, 3, 6], player = player) or \
           are_same_places([1, 4, 7], player = player) or \
           are_same_places([2, 5, 8], player = player) or \
           are_same_places([0, 4, 8], player = player) or \
           are_same_places([2, 4, 6], player = player)

def is_draw() :
    return UNOCCUPIED not in board

print_board()
current_player = PLAYER_X

while True :
    user_input = input("Your turn player {} : ".format(current_player)).strip()
    user_input_index = (int (user_input)) - 1
    
    if not is_valid_place(user_input_index) :
        print("Invalid move!")
        continue

    board[user_input_index] = current_player
    print_board()

    if has_won(current_player) :
        print("Player {} won! Congrats!".format(current_player))
        break

    if is_draw() :
        print("The Game is DRAW!")
        break
    
    current_player = next_player(current_player)
    
