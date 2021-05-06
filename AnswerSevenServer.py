# Modern Bank - ATM Application
# server

import pyrebase
import socket
from _thread import *
import threading
import time
import os
from os import system, name

print_lock = threading.Lock()


def clear():
    os.system('cls')


def welcome():
    smoke = ['               (_)', '               ()', '                ()', '               ()', '                ()']
    print("\n" * 4)
    print("                _     ")
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Modern Bank   \\")
    print("  |    ing system!!!    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print("")
    time.sleep(.6)
    clear()

    print("\n" * 5)
    print(smoke[0])
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Modern Bank   \\")
    print("  |    ing system!!!    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print("")
    time.sleep(.6)
    clear()

    print("\n" * 4)
    print(smoke[1])
    print(smoke[0])
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Modern Bank   \\")
    print("  |    ing system!!!    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print("")
    time.sleep(.6)
    clear()

    print("\n" * 3)
    print(smoke[2])
    print(smoke[1])
    print(smoke[0])
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Modern Bank   \\")
    print("  |    ing system!!!    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print("")
    time.sleep(.6)
    clear()

    print("\n" * 2)
    print(smoke[3])
    print(smoke[2])
    print(smoke[1])
    print(smoke[0])
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Modern Bank   \\")
    print("  |    ing system!!!    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print("")
    time.sleep(.6)
    clear()

    print("\n" * 1)
    print(smoke[4])
    print(smoke[3])
    print(smoke[2])
    print(smoke[1])
    print(smoke[0])
    print("     __________| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /     A Modern Bank   \\")
    print("  |    ing system!!!    |")
    print("  |     ____     ___    |")
    print("  |    |    |   |___|   |")
    print("__|____|____|___________|__")
    print("")
    time.sleep(.6)
    clear()


# thread function
def threaded(c):
    global name
    while True:

        firebaseConfig = {
            "apiKey": "AIzaSyA3QR5xAFUKdS8TC3cTIhEVvlR6r3ITwAY",
            "authDomain": "pythonatm-bank.firebaseapp.com",
            "storageBucket": "pythonatm-bank.appspot.com",
            "databaseURL": "https://pythonatm-bank-default-rtdb.firebaseio.com/"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)

        auth = firebase.auth()
        db = firebase.database()

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        print("Choose 1,2,3......")
        print("1.SignIN")
        print("2.SignUP")
        print("3.EXIT")
        intended = input()

        while True:
            print(intended)
            if intended == "2":
                email = input("Please enter your mail address:\n")
                password = input("Please enter your pass (8 letters - upper, uniqe and numbers combines):\n")
                name = input("Please enter your full identical name:\n")

                user = auth.create_user_with_email_and_password(email, password)
                balance = 5000

                data = {"email": email, "balance": balance}
                db.child("users").child(name).set(data)

                balancecurrent = db.child("users").child(name).child("balance").get()
                namecurrent = db.child("users").child(name).get()

                print("Success...")
                print("Hi", namecurrent.val(), ",Welcome!")
                break

            elif intended == "1":
                email = input("Please enter your mail address:\n")
                password = input("Please enter your pass:\n")

                user = auth.sign_in_with_email_and_password(email, password)

                print("Success...")
                print("Hi", email, ",Welcome back!")
                break

            elif intended == "3":
                break
        # bonus section
        user = firebase.auth().current_user
        if user:
            welcome()
            # Check balance
            if data == b'1':
                # send back balance to client
                balancecurrent = db.child("users").child(name).child("balance").get()
                print(balancecurrent.val())
                c.send(bytes(str(balancecurrent.val()), 'utf8'))
            # Withdraw
            if data == b'2':
                balancecurrent = db.child("users").child(name).child("balance").get()
                withdrawal = c.recv(1024)
                print("Withdraw: ", str(withdrawal, 'utf8'))
                # Check if withdrawal amount is more than current balance.
                if int(withdrawal) < balancecurrent.val():
                    balance = balancecurrent.val() - int(withdrawal)
                    print("New balance: ", balance)
                    db.child("users").child(name).child("balance").set(balance)
                    c.send(bytes(str(balance), 'utf8'))
                else:
                    print("Withdrawal amount larger then current balance.")
                    c.send(bytes("No", 'utf8'))
            # Deposit
            if data == b'3':
                balancecurrent = db.child("users").child(name).child("balance").get()
                deposit = c.recv(1024)
                print("Deposit: ", str(deposit, 'utf8'))
                balance = balancecurrent.val() + int(deposit)
                print("New balance: ", balance)
                db.child("users").child(name).child("balance").set(balance)
                c.send(bytes(str(balance), 'utf8'))
            firebase.getInstance().signOut()
        else:
            print("Cannot transact with the user so the session will be closed!....\n ")
            time.sleep(0.6)
            print("Try to log out from other place and log back in here.....\n ")
            time.sleep(0.6)
            print("3")
            time.sleep(0.6)
            print("2")
            time.sleep(0.6)
            print("1")
            time.sleep(0.6)
            print("Closed.")
            firebase.getInstance().signOut()
            break

        # connection closed
    c.close()


def Main():
    host = "192.168.56.1"

    # reserve a port on your computer
    port = 5050
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # loop until client exits
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
