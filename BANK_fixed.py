import time
import json
import subprocess
import sys

# Menu Variable
menu = '''
    --BANK LOL--
    --What do you want to do today?--
    ---------------------------------
    1. View my bank account
    2. Send money to other bank account
    3. My credits
    4. Take out a loan (credit or smth)
    5. Exit
'''

# Balance
balance = 15000
loan_amount = 0  # Добавим переменную для отслеживания кредита

# Clear shell func
def clear():
    subprocess.run('cls' if sys.platform == 'win32' else 'clear', shell=True)

# Back func
def back():
    time.sleep(1)
    clear()
    print(menu)

# Loan function
def loan(amount):
    global balance, loan_amount
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be positive!")
            return
        
        balance += amount
        loan_amount += amount
        print(f"Done! Your bank account now - {balance}")
        print(f"Your total loan: {loan_amount}")
    except ValueError:
        print("Please enter a valid number!")

# Send money function
def send_money():
    global balance
    while True:
        clear()
        print("--Send Money--")
        print(f"Your balance: {balance}")
        print("-- Type 'back' to return --")
        
        amount = input("Enter amount to send: ")
        if amount.lower() == 'back':
            back()
            return
        
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive!")
                time.sleep(1)
                continue
                
            if amount > balance:
                print("Error: Not enough funds!")
                time.sleep(1)
                continue
                
            recipient = input("Enter recipient's card number (16 digits): ")
            if len(recipient) != 16 or not recipient.isdigit():
                print("Invalid card number!")
                time.sleep(1)
                continue
                
            balance -= amount
            print(f"Successfully sent {amount} to {recipient}")
            print(f"New balance: {balance}")
            time.sleep(2)
            back()
            return
        except ValueError:
            print("Please enter a valid number!")
            time.sleep(1)

# Registration
time.sleep(1)
print("Welcome to BANK LOL")
print("--Registration--")

name = input("Your full name: ")
login = input("Login: ")
password = input("Password: ")

# Save data
user_data = {
    "name": name,
    "login": login,
    "password": password,
    "balance": balance,
    "loan": loan_amount
}

# Сохраняем в JSON-файл
with open("user_data.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)

# Reading JSON
try:
    with open("user_data.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
except FileNotFoundError:
    print("Error loading user data!")
    sys.exit(1)

# Menu
time.sleep(1)
clear()
print(menu)

while True:
    mchoose = input("Choose: ")

    # Logic
    if mchoose == "1":
        clear()
        print("Name:", loaded_data["name"])
        print("Login:", loaded_data["login"])
        # Не показываем пароль для безопасности
        print(f'Balance: {balance}')
        print(f'Loan: {loan_amount}')
        input("\nPress Enter to return...")
        back()

    elif mchoose == "2":
        send_money()  # Используем новую функцию для отправки денег

    elif mchoose == "3":
        clear()
        print("-- My Credits --")
        print(f"Your current loan: {loan_amount}")
        input("\nPress Enter to return...")
        back()

    elif mchoose == "4":
        clear()
        print("-- ARE YOU SURE? --")
        print("By taking out a loan*, you assume the obligation to repay them within 7 days.")
        print("\n*Of course, the loan is not real, it's just my code for learning Python.")
        SURE = input("Y/N: ").lower()
        
        if SURE == "y":
            clear()
            anm = input("Loan amount: ")
            loan(anm)  # Используем исправленную функцию кредита
            input("\nPress Enter to return...")
            back()

    elif mchoose == "5":
        print("Goodbye!")
        time.sleep(1)
        sys.exit(0)

    elif mchoose.lower() == "back":
        back()

    else:
        print("Invalid option!")
        time.sleep(1)
        clear()
        print(menu)
