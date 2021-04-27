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

# Section a
sumint = 0
while True:
    number = input("Please enter a valid number or stop to stop the program ")
    if number == "stop":
        break
    try:
        sumint = sumint + int(number)
    except ValueError:
        print("Enter a valid number or stop the program, faggot...................")

print("sum = " + str(sumint))

# Section b
def sum_digits(digit):
    s = sum(int(x) for x in str(digit) if x.isdigit())
    if len(str(s)) > 1:
        return sum_digits(s) + s
    else:
        return s

def main():
    listofnums = input("Please enter list of numbers with '' or without ")
    sum = sum_digits(listofnums)
    print("sum = " + str(sum))

if __name__ == "__main__":
    main()
