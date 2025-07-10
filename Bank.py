class Bank:
    def __init__(self, account_number, account_holder, initial_balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type.lower()
        self.__balance = initial_balance
        self.__is_active = True

    def __str__(self):
        return (f"Account Number: {self.account_number}, \n"
                f"Account Holder: {self.account_holder}, \n"
                f"Account Type: {self.account_type.capitalize()}, \n"
                f"Balance: ${self.__balance:.2f}, \n"
                f"Active: {self.__is_active}")

    def Deactivate(self):
        if self.__is_active:
            self.__is_active = False
            print(f"Account {self.account_number} deactivated.")
        else:
            print(f"Account {self.account_number} is already inactive.")


if __name__ == "__main__":
    # Example usage
    bank_account = {}
    account_number = 101
    while True:
        print("\n=== Bank Account Menu ===")
        print("1. Create Account")
        print("2. Show all Account Details")
        print("3. View Account Details by Number")
        print("4. Deactivate Account")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                holder = input("Enter account holder name: ")
                while True:
                    print("Enter account type (Savings/Current): ")
                    print("1. Savings")
                    print("2. Current")

                    account_type_choice = int(input("Choose account type: "))       
                    if account_type_choice == 1:
                        account_type = 'savings'
                        break
                    elif account_type_choice == 2:
                        account_type = 'current'
                        break
                    else:
                        print("Invalid choice. Please enter 1 for Savings or 2 for Current.")


                initial_balance = float(input("Enter initial balance: "))

                if account_type == 'current' and initial_balance < 100000:
                    print("Current accounts require a minimum balance of ₹100000.")
                    continue

                bank_account[account_number] = Bank(account_number, holder, initial_balance, account_type)
                print(f"Account created with number {account_number}")
                account_number += 1


            case 2:
                password = input("Enter password to view account balances: ")
                if password == "admin":
                    print("Account Balances:")
                    for acc_num, acc in bank_account.items():
                        print(f"Account Number: {acc_num}, "
                            f"Type: {acc.account_type.capitalize()}, "
                            f"Balance: ${acc._Bank__balance:.2f}")
                else:
                    print("Incorrect password. Access denied.")

            case 3:
                # if account deactived, we should not allow viewing details of that account
                acc_num = int(input("Enter account number to view details: "))
                if acc_num in bank_account:
                    print(bank_account[acc_num])
                else:
                    print("Account not found.")
            
            case 4:
                acc_num = int(input("Enter account number to deactivate: "))
                if acc_num in bank_account:
                    bank_account[acc_num].Deactivate()
                else:
                    print("Account not found.")

            case 5:
                print("Exiting the program.")
                break

            case _:
                print("Invalid choice, please try again.")