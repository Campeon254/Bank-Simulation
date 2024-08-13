# creating an account
"""
This function accepts the user input for the User name.
It the prompts the user to enter a password and confirms the password.
If the two passwords entered match, then it creates a file named 'accounts.txt' in append mode('a')
The file object created is assigned to the file variable.
The function then writes the username and password to the file in the format 'username:password'.
Finally, it prints a success message.
If the passwords do not match, it prints an error message.
"""
balance = 0.0
def sign_up(): # type: ignore
    balance = 0.0
    username = input('Enter your Username:')
    with open("accounts.txt", "a+") as account_file:
        account_file.seek(0)# this moves the cursor to the 0 position to allow reading
        for line in account_file:
            if line.startswith(username + ":"):
                print("Username already exists")
                return
                
            if username.strip() == " ":
                print('Invalid Username. Try Again.')
                return

        password = input('Create a strong Password:')
        confirm_password = input('Confirm your Password:')
        if password == confirm_password:
            account_file.write(f'{username}:{password}:{balance}\n')
            print("Account Created Successfully")
                    
        else:
            print("Passwords do not match. Please try again.")
        
sign_up()

# create a function sign in
"""
This function allows the user to put in their username and password.
The function checks if the username and password are correct.
If they are correct, it returns a welcome message with the username.
If they are not correct, it returns an error message.
The function then proceeds to offer the following options for the user:
    1) deposit
    2) withdraw
    3) check balance
    4) exit
The user has those options. If an invalid option is put, then it brings a warning message.
If the user tries to withdraw more money than is available in their account, it also brings a warning.
"""

def sign_in():
    global  balance
    username = input("Enter your username: ")
    password = input("Enter your password: ")
        
    with open("accounts.txt", "r") as account_file:
        for line in account_file:
            if line.strip().startswith(f"{username}:{password}"):
                # extract the current balance from the line in the file
                balance = float(line.strip().split(":")[2])
                print('Login Successful!')
                print(f"Welcome {username}!")
                return perform_transaction(username) # type: ignore
                            
            print("Incorrect username or password. Please try again.")
            return


    def perform_transaction(username):
        global balance
        while True:
            print("\nOptions:")
            print("1) Deposit")
            print("2) Withdraw")
            print("3) Check Balance")
            print("4) Exit")

            choice = input("Enter an option")
            if choice == "1":
                amount = float(input("Enter the amount to deposit: $"))
                balance += amount
                print(f"{amount} deposited successfully. Your new balance is {balance}.")

            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: $"))
                if amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"{amount} withdrawn successfully. Your new balance is {balance}.")

            elif choice == "3":
                print(f"Your current balance is {balance}")
            
            elif choice == "4":
                print("Thank you for using our services. Goodbye!")
                # update the balance before exiting
                update_account_balance(username)
                break
            else:
                print("Invalid option. Please try again.")

    def update_account_balance(username):
        lines = []
        with open("accounts.txt", "r") as account_file:
            lines = account_file.readlines()

        with open("accounts.txt", "w") as account_file:
            for line in lines:
                if line.startswith(username + ":"):
                    parts = line.strip().split(":")
                    parts[2] = str(balance)
                    account_file.write(":".join(parts)+ "\n")
                else:
                    account_file.write(line)

    sign_in()



