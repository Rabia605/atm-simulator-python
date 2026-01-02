import os
import time
import logging
from datetime import datetime


logging.basicConfig(
    filename="reference.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


USERS = {
    1234: {
        "name": "Rabia Noreen",
        "balance": 10000
    },
    1122: {
        "name": "Raffay",
        "balance": 15000
    },
    1133: {
        "name": "Sara",
        "balance": 12000
    },
    1803: {
        "name": "Ahmed",
        "balance": 20000
    },
    1672: {
        "name": "Hassan",
        "balance": 8000
    },
    1110: {
        "name": "Ayesha",
        "balance": 17500
    },
    1111: {
        "name": "Umer",
        "balance": 11000
    }
}


current_user = None


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_datetime():
    print(datetime.now().strftime("%A, %d %B %Y | %I:%M:%S %p"))


def authenticate():
    global current_user

    attempts = 3

    while attempts > 0:
        try:
            pin = int(input("Enter your PIN: "))

            if pin in USERS:
                current_user = USERS[pin]

                print(f"\nWelcome, {current_user['name']}!")
                time.sleep(1)

                return True

            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")

        except ValueError:
            print("Please enter numbers only.")

    print("\nToo many incorrect attempts.")
    return False


def check_balance():
    balance = current_user["balance"]

    print("\n" + "=" * 40)
    print("           ACCOUNT BALANCE")
    print("=" * 40)
    print(f"\nAccount Holder: {current_user['name']}")
    print(f"Available Balance: Rs. {balance:,}")

    logging.info(
        f"Transaction: CHECK BALANCE | User: {current_user['name']}"
    )


def withdraw():
    try:
        amount = int(input("\nEnter the amount to withdraw: "))

        if amount <= 0:
            print("Please enter a valid amount.")
            return

        if amount > current_user["balance"]:
            print("Insufficient balance.")
            return

        print("\nTransaction processing...")
        time.sleep(1)

        current_user["balance"] -= amount

        print(f"\nRs. {amount:,} withdrawn successfully.")
        print(f"Remaining balance: Rs. {current_user['balance']:,}")

        logging.info(
            f"Transaction: WITHDRAW | "
            f"User: {current_user['name']} | "
            f"Amount: Rs. {amount}"
        )

    except ValueError:
        print("Please enter a valid amount.")


def transfer():
    account = input(
        "\nEnter the receiver's account number: "
    ).strip()

    if not account.isdigit() or len(account) != 10:
        print("Invalid account number.")
        print("Account number must contain exactly 10 digits.")
        return

    try:
        amount = int(input("Enter the amount to transfer: "))

        if amount <= 0:
            print("Please enter a valid amount.")
            return

        if amount > current_user["balance"]:
            print("Insufficient balance.")
            return

        print("\nProcessing transfer...")
        time.sleep(1)

        current_user["balance"] -= amount

        print(f"\nRs. {amount:,} transferred successfully.")
        print(f"Remaining balance: Rs. {current_user['balance']:,}")

        logging.info(
            f"Transaction: TRANSFER | "
            f"User: {current_user['name']} | "
            f"Account: {account} | "
            f"Amount: Rs. {amount}"
        )

    except ValueError:
        print("Please enter a valid amount.")


def transaction_menu():
    while True:
        clear_screen()
        show_datetime()

        print("\n" + "=" * 40)
        print(f"       WELCOME, {current_user['name'].upper()}")
        print("=" * 40)
        print("  1.  Check Balance")
        print("  2.  Withdraw Cash")
        print("  3.  Transfer Money")
        print("  4.  Exit")
        print("=" * 40)

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            check_balance()

        elif choice == "2":
            withdraw()

        elif choice == "3":
            transfer()

        elif choice == "4":
            print(f"\nThank you, {current_user['name']}!")
            print("Have a great day!")
            break

        else:
            print("\nInvalid selection.")
            print("Please choose an option from 1 to 4.")

        input("\nPress Enter to return to the main menu...")


def main():
    clear_screen()
    show_datetime()

    print("\n" + "=" * 40)
    print("             ATM MACHINE")
    print("=" * 40)

    if authenticate():
        transaction_menu()
    else:
        print("\nYour account has been locked.")


if __name__ == "__main__":
    main()