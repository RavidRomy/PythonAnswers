################################
# Python Answer for Question 7 #
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

# Modern Bank - ATM Application based client-server system
# client

import socket


def Main():
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "Disconnected"
    SERVER = "192.168.56.1"
    ADDR = (SERVER, PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDR)

    while True:
        # ask options
        ans = input('\nWhat would you like to do?'
                    '\n1: Check balance'
                    '\n2: Withdrawal'
                    '\n3: Deposit'
                    '\nq: End the current session\n: ')
        # Check balance
        if ans == '1':
            s.send(ans.encode('ascii'))
            data = s.recv(1024)
            print('\nCurrent balance :', str(data, 'utf8'))
            continue
        # Withdraw
        if ans == '2':
            s.send(ans.encode('ascii'))
            withdraw = input('\n How much to withdrawal? : ')
            s.send(withdraw.encode('ascii'))
            data = s.recv(1024)
            if data == b'No':
                print("\nNot enough funds.")
            else:
                print('\nBalance after withdrawal :', str(data, 'utf8'))
            continue
        # Deposit
        if ans == '3':
            s.send(ans.encode('ascii'))
            deposit = input('\n How much to deposit? : ')
            s.send(deposit.encode('ascii'))
            data = s.recv(1024)
            print('\nBalance after withdrawal :', str(data, 'utf8'))
            continue
        # Quits session
        if ans == 'q':
            print("\nEnding session")
            break
        else:
            print("\nNot a valid input, try again.")
            continue
    # close the connection
    s.close()


if __name__ == '__main__':
    Main()
