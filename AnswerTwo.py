################################
# Python Answer for Question 2 #
# ====== BY HEISENBERG ======= #
###### . - - - - - - - - . #####
###### |                 | #####
#### ----= ___________ =---- ###
######## ___        ___ ########
#######_| ___) == (___ |_#######
#########\     ***     /########
##########\   * = *   /#########
###########\  *****  /##########
################################

board = [[1, 1, 1],
         [2, 2, 2],
         [2, 0, 2], ]


def win_check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == num:
            continue
        else:
            break
    else:
        return True


def main():
    if win_check(1):
        won1 = True
    else:
        won1 = False
    if win_check(2):
        won2 = True
    else:
        won2 = False

    if won1 == won2:
        print("Tie")
    elif won1:
        print("Won 1")
    elif won2:
        print("Won 2")


if __name__ == "__main__":
    main()
