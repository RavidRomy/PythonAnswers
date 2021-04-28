################################
# Python Answer for Question 3 #
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


def shrink_str(strr):
    n = len(strr)
    i = 0
    while i < n - 1:
        count = 1
        while i < n - 1 and strr[i] == strr[i + 1]:
            count += 1
            i += 1
        i += 1
        print(strr[i - 1] + str(count), end='')


def main():
    somestring = "abcaadddcc"
    shrink_str(somestring)

if __name__ == "__main__":
    main()
