################################
# Python Answer for Question 5 #
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


def multi(x):
    return x * 2


def Map(f, listt):
    n = len(listt) -1
    while n >= 0:
        print(f(listt[n]))
        n -= 1


def main():
    listoftemps = [9, 4, 6, 8, 10]
    Map(multi, listoftemps)


if __name__ == "__main__":
    main()
