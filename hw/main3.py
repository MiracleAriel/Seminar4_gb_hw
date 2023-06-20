# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

operations_history = []  # Список операций поступления и снятия средств


def deposit(amount, balance):
    balance += amount
    operations_history.append(f"Пополнение на сумму {amount}")
    return balance


def withdraw(amount, balance):
    if amount <= balance:
        balance -= amount
        operations_history.append(f"Снятие на сумму {amount}")
    else:
        operations_history.append("Недостаточно средств")
    return balance


def check_balance(balance):
    print(f"Текущий баланс: {balance}")


# Использование функций
current_balance = 0

current_balance = deposit(100, current_balance)
current_balance = withdraw(50, current_balance)
current_balance = deposit(200, current_balance)
current_balance = withdraw(300, current_balance)

check_balance(current_balance)

print("История операций:")
for operation in operations_history:
    print(operation)
