def atm():
    balance = 0
    count = 0
    transactions = []

    def deposit(amount):
        nonlocal balance, count, transactions
        if balance >= 5000000:
            balance -= balance * 0.1
        balance += amount
        count += 1
        if count % 3 == 0:
            balance -= balance * 0.03
        transactions.append(f"Пополнение: +{amount}")

    def withdraw(amount):
        nonlocal balance, count, transactions
        if balance >= 5000000:
            balance -= balance * 0.1
        if amount > balance:
            print("Недостаточно средств на счете.")
            return
        if amount > 600:
            amount = 600
        elif amount < 30:
            amount = 30
        balance -= amount + (amount * 0.015)
        count += 1
        if count % 3 == 0:
            balance -= balance * 0.03
        transactions.append(f"Снятие: -{amount}")

    while True:
        action = input("Выберите действие (пополнить, снять, выйти): ")
        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 != 0:
                print("Сумма пополнения должна быть кратна 50.")
                continue
            deposit(amount)
        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                print("Сумма снятия должна быть кратна 50.")
                continue
            withdraw(amount)
        elif action == "выйти":
            break
        else:
            print("Некорректное действие. Попробуйте снова.")

    print("Текущий баланс:", balance)
    print("Список операций:", transactions)

atm()