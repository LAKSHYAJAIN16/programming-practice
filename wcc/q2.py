t = int(input())

def winning(board_1, board_2, board_3, move):
    # Check the lines
    if board_1[0] == move and board_1[1] == move and board_1[2] == move:
        return True
    if board_2[0] == move and board_2[1] == move and board_2[2] == move:
        return True
    if board_3[0] == move and board_3[1] == move and board_3[2] == move:
        return True
    
    # Check the columns
    if board_1[0] == move and board_2[0] == move and board_3[0] == move:
        return True
    if board_1[1] == move and board_2[1] == move and board_3[1] == move:
        return True
    if board_1[2] == move and board_2[2] == move and board_3[2] == move:
        return True
    
    # Check the diagonals
    if board_1[0] == move and board_2[1] == move and board_3[2] == move:
        return True
    if board_1[2] == move and board_2[1] == move and board_3[0] == move:
        return True
    
    return False

outs = []
for k in range(t):
    board_1 = list(map(str,input()))
    board_2 = list(map(str,input()))
    board_3 = list(map(str,input()))
    move = input()[0]
    found = False
    for m in range(3):
        if board_1[m] == ".":
            board_1_copy = board_1
            board_1[m] = move
            if winning(board_1_copy, board_2, board_3, move) == True:
                outs.append(move + " can win")
                found = True
                break
            board_1[m] = "."
        if board_2[m] == ".":
            board_2_copy = board_2
            board_2[m] = move
            if winning(board_1, board_2_copy, board_3, move) == True:
                outs.append(move + " can win")
                found = True
                break
            board_2[m] = "."
        if board_3[m] == ".":
            board_3_copy = board_3
            board_3[m] = move
            if winning(board_1, board_2, board_3_copy, move) == True:
                outs.append(move + " can win")
                found = True
                break
            board_3[m] = "."
    if found == False:
        outs.append("no winning move")
        
for out in outs:
    print(out)