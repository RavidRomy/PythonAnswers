################################
# Python Answer for Question 4 #
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


def check_id(idnum):
    if len(idnum) != 9:
        return False
    list()
    try:
        idvalue = list(map(int, idnum))
    except:
        return False
    counter = 0
    for i in range(9):
        idvalue[i] *= (i % 2) + 1
        if idvalue[i] > 9:
            idvalue[i] -= 9
        counter += idvalue[i]
    if counter % 10 == 0:
        return True
    else:
        return False

def main():
    print(check_id("543700421"))
    print(check_id("322248097"))
    print(check_id("322248093"))
    print(check_id("059807578"))

if __name__ == "__main__":
    main()