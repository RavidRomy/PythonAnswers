################################
# Python Answer for Question 1 #
# ====== BY HEISENBERG ======= #
###### . - - - - - - - - . #####
###### |                 | #####
#### ----= ___________ =---- ###
######## ___        ___ ########
####### | ___)  = (___ | #######
#############  *** #############
############# * = * ############
############# ***** ############
################################


# Section b
def sum_digits(listofdigits):
    return sum(int(x) for x in str(listofdigits) if x.isdigit())


def main():
    # Section a
    sumint = 0
    while True:
        number = input("Please enter a valid number or stop to stop the program: \n")
        if number == "stop":
            break
        try:
            sumint = sumint + int(number)
        except ValueError:
            print("Enter a valid number or stop the program, faggot................... \n")

    print("sum = " + str(sumint))

    listofnums = input("Please enter list of numbers with '' or without: \n")
    sum = sum_digits(listofnums)
    print("sum = " + str(sum))


if __name__ == "__main__":
    main()
