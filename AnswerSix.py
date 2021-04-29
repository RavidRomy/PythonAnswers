################################
# Python Answer for Question 6 #
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
import time


def memoize(function):
    memo = []

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            vector = function(*args)
            memo[args] = vector
            return vector

    return wrapper


@memoize
def multi(x):
    time.sleep(6)
    return x*2
