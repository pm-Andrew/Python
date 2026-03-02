# PS1 Math interperter Example ps1_ex.py
# Bruce/ Andrew


def main():
    balance = 0
    while True:
        command = input().strip()
        if command != "":
            action, amount = command.split(" ")
        if action == "deposit":
            balance = balance + float(amount)
        elif action == "withdrawl":
            if float(amount) <= balance:
                balance = balance - float(amount)
            else:
                print("Insufficient funds")
            print(f"Balance: ${balance:.2f}")
        else:
            break
main()
