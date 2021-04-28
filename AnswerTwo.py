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

game = [[2, 2, 2],
        [2, 1, 2],
        [1, 0, 2], ]

def win(current_game):
    global item, row
    counter = 0
    for row in game:
        #print(row)
        all_match = True
        counter += 1
        for item in row:
            #print("item = ", item, "row = ", row[0])
            if item != row[0]:
                all_match = False
                counter -= 1
        if all_match:
            print("Game player", item, "winner!!!")
    if counter == 2 and game[0][0] != game[1][0] or game[1][0] != game[2][0]:
        print(game[0][0], game[1][0])
        print("Two won then it's Tie")
    return -1


x = win(game)
print(x)

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
if diags[0] == diags[1] == diags[2]:
    print("Winner! = ", diags[0])

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("Winner! = ", check[0])
