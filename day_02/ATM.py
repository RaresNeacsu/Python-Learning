def reset(balance):
    res= input("Do you want to perform another action? (yes/no)")
    if res == "yes":
        print("The ATM has been reset.")
        atm_menu(balance)
    elif res == "no":
        exit_program()
    else:
        print("Invalid input, please try again.")
        reset(balance)
def exit_program():
    print("Exiting the ATM.")
    exit()
def check_balance(balance):
    print(f"Your current balance is ${balance}.")
    reset(balance)
def deposit_money(balance):
    amount = float(input("Enter the amount to deposit: $"))
    balance += amount
    print(f"You have successfully deposited ${amount}. Your new balance is ${balance}.")
    reset(balance)
def withdraw_money(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > 1000:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"You have successfully withdrawn ${amount}. Your new balance is ${balance}.")
    reset(balance)
def atm_menu(balance):
    print("Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Please choose an option (1-4): ")

    if choice == '1':
        check_balance(balance)
    elif choice == '2':
        deposit_money(balance)
    elif choice == '3':
        withdraw_money(balance)
    elif choice == '4':
        exit_program()
    else:
        print("Invalid choice, please try again.")
        atm_menu(balance)

balance = 1000 
code=input("Please input your PIN to access the ATM: ")
if code == "2354":
    atm_menu(balance)