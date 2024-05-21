class ExpenseSharingApp:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = 0.0
            print(f"User {name} added.")
        else:
            print(f"User {name} already exists.")

    def add_expense(self, payer, amount, participants):
        if payer not in self.users:
            print(f"Payer {payer} does not exist.")
            return

        amount_per_person = amount / len(participants)
        for participant in participants:
            if participant not in self.users:
                print(f"Participant {participant} does not exist.")
                return

        self.expenses.append({'payer': payer, 'amount': amount, 'participants': participants})

        for participant in participants:
            if participant == payer:
                self.users[participant] += (amount - amount_per_person)
            else:
                self.users[participant] -= amount_per_person

        print(f"Expense of {amount} added. {payer} paid for {', '.join(participants)}.")

    def show_balances(self):
        print("\nCurrent Balances:")
        for user, balance in self.users.items():
            print(f"{user}: {balance:.2f}")
        print("")

    def show_summary(self):
        print("\nSummary of who owes whom:")
        for expense in self.expenses:
            payer = expense['payer']
            amount = expense['amount']
            participants = expense['participants']
            amount_per_person = amount / len(participants)
            for participant in participants:
                if participant != payer:
                    print(f"{participant} owes {payer}: {amount_per_person:.2f}")
        print("")

if __name__ == "__main__":
    app = ExpenseSharingApp()

    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. Add Expense")
        print("3. Show Balances")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter user name: ")
            app.add_user(name)
        elif choice == "2":
            payer = input("Enter the name of the payer: ")
            amount = float(input("Enter the amount paid: "))
            participants = input("Enter the names of participants (comma separated): ").split(", ")
            app.add_expense(payer, amount, participants)
        elif choice == "3":
            app.show_balances()
        elif choice == "4":
            app.show_summary()
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid option, please try again.")
