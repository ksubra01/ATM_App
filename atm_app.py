import streamlit as st

class Bank:
    def __init__(self):
        # Simulate a database of account information
        self.accounts = {
            '1234': {'pin': '4321', 'balance': 1000},
            '5678': {'pin': '8765', 'balance': 1500},
            '9012': {'pin': '2109', 'balance': 2000},
            '3456': {'pin': '6543', 'balance': 2500},
            '7890': {'pin': '0987', 'balance': 3000},
            '2345': {'pin': '5432', 'balance': 3500},
            '6789': {'pin': '9876', 'balance': 4000},
            '0123': {'pin': '3210', 'balance': 4500},
            '4567': {'pin': '7654', 'balance': 5000},
            '8901': {'pin': '1098', 'balance': 5500}
        }

    def validate_pin(self, card_number, pin):
        # Simulate checking PIN against bank records
        if card_number in self.accounts:
            return pin == self.accounts[card_number]['pin']
        else:
            return False

    def get_balance(self, card_number):
        return self.accounts[card_number]['balance']

    def deposit(self, card_number, amount):
        self.accounts[card_number]['balance'] += amount

    def withdraw(self, card_number, amount):
        if self.accounts[card_number]['balance'] >= amount:
            self.accounts[card_number]['balance'] -= amount
            return amount
        else:
            return 0


class ATM:
    def __init__(self):
        self.bank = Bank()
        self.card_number = None

    def insert_card(self, card_number):
        self.card_number = card_number

    def enter_pin(self):
        pin = st.text_input(f"Enter your PIN for card number {self.card_number}:")
        return pin

    def select_account(self):
        # In a real ATM, there might be multiple accounts associated with a card,
        # but for simplicity, we assume there's only one account per card
        return self.card_number

    def check_balance(self):
        return self.bank.get_balance(self.card_number)

    def deposit(self, amount):
        self.bank.deposit(self.card_number, amount)

    def withdraw(self, amount):
        return self.bank.withdraw(self.card_number, amount)


# Main function to interact with ATM
def main():
    atm = ATM()

    st.title("ATM Simulator")

    card_number = st.text_input("Enter your card number:")
    atm.insert_card(card_number)

    pin_entered = False
    while not pin_entered:
        pin = atm.enter_pin()
        if pin:
            pin_entered = atm.bank.validate_pin(atm.card_number, pin)
            if not pin_entered:
                st.error("Incorrect PIN. Please try again.")

    st.write("PIN accepted. Choose an option:")

    choice = st.selectbox("Select an option:", ["Check Balance", "Deposit", "Withdraw"])
    if choice == "Check Balance":
        st.write("Current Balance:", atm.check_balance())
    elif choice == "Deposit":
        amount = st.number_input("Enter deposit amount:", min_value=0)
        if st.button("Deposit"):
            atm.deposit(amount)
            st.write("Deposit successful. Current Balance:", atm.check_balance())
    elif choice == "Withdraw":
        amount = st.number_input("Enter withdrawal amount:", min_value=0)
        if st.button("Withdraw"):
            withdrawn_amount = atm.withdraw(amount)
            if withdrawn_amount > 0:
                st.write("Withdrawn amount:", withdrawn_amount)
                st.write("Current Balance:", atm.check_balance())
            else:
                st.write("Insufficient funds.")


if __name__ == "__main__":
    main()
