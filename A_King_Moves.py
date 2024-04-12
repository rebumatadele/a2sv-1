def king_moves():
    board = list(input())
    x = board[0]
    y = int(board[1])
    moves=8
    if((x == 'a' or x=='h') and (y==1 or y==8)):
        moves -=5
    elif((x == 'a' or x=='h') and (y!=1 or y!=8) or (x != 'a' or x!='h') and (y==1 or y==8)):
        moves -=3
    elif((x != 'a' or x!='h') and (y!=1 or y!=8)):
        moves = 8
    print(moves)
king_moves()
        