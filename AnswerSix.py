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


def main():
    print("Run console to check this exercise..............")
    print("*Then import this exercise and call multi on whatever you want.*")
    print("$$$$$$ . - - - - - - - - . $$$$$")
    print("$$$$$$ |                 | $$$$$")
    print("$$$$ ----= ___________ =---- $$$")
    print("$$$$$$$$ ___        ___ $$$$$$$$")
    print("$$$$$  _| ___) == (___ |_  $$$$$")
    print("$$$$$$$$ \     ###     / $$$$$$$")
    print("$$$$$$$$$ \   # = #   / $$$$$$$$")
    print("$$$$$$$$$$ \  #####  / $$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    s = input("Say my name: ")
    if s == "HEISENBERG":
        print("That's true!")
    else:
        print("Pulling out the gun!")


if __name__ == "__main__":
    main()
