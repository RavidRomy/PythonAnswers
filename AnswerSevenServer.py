#server

import pyrebase
import socket
import threading


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

firebaseConfig = {
    "apiKey": "AIzaSyA3QR5xAFUKdS8TC3cTIhEVvlR6r3ITwAY",
    "authDomain": "pythonatm-bank.firebaseapp.com",
    "storageBucket": "pythonatm-bank.appspot.com",
    "databaseURL": "https://pythonatm-bank-default-rtdb.firebaseio.com/"
  }


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()


print("1.SignIN")
print("2.SignUP")
print("3.EXIT")
intended = input()

while True:
    if intended == 2:
        email = input("Please enter your mail address:\n")
        password = input("Please enter your pass (8 letters - upper, uniqe and numbers combines):\n")
        name = input("Please enter your full identical name:\n")
        amount = 0

        user = auth.create_user_with_email_and_password(email, password)

        data = {"name": name, "amount": amount}
        db.child(email).set(data)

        print("Success...")
        print("Hi", name + ",", "Welcome!")

    elif intended == 1:
        email = input("Please enter your mail address:\n")
        password = input("Please enter your pass:\n")

        user = auth.sign_in_with_email_and_password(email, password)

        print("Success...")
        print("Hi", db.child(email).child("name").get() + ",", "Welcome back!")

    elif intended == 2:
        break
