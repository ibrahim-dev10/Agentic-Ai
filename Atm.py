stored_pin = "1234"
attempts = 0
max_attempts = 4

while attempts < max_attempts:
    pin = input("Enter your PIN code: ")

    if pin == stored_pin:
        print("PIN matched successfully!")

        amount = float(input("Enter the amount you want to withdraw: "))

        balance = 10000

        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")

        break

    else:
        attempts += 1
        remaining = max_attempts - attempts

        if remaining > 0:
            print("Incorrect PIN! Attempts remaining:", remaining)
        else:
            print("Maximum attempts reached. Your account is locked.")