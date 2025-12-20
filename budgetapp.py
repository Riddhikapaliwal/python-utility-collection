class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})

            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, target_category):

        if self.check_funds(amount):

            transfer_out_description = f"Transfer to {target_category.name}"
            self.withdraw(amount, transfer_out_description)

            transfer_in_description = f"Transfer from {self.name}"
            target_category.deposit(amount, transfer_in_description)

            return True
        else:

            return False

    def get_balance(self):
        balance = 0
        for bal in self.ledger:
            balance += bal["amount"]
        return balance

    def __str__(self):
        title = self.name.center(30, '*')
        lines = [title]
        for items in self.ledger:
            lines.append(f"{items['description'][:23]:<23}{items['amount']:>7.2f}")
        lines.append(f"Total: {self.get_balance()}")
        return "\n".join(lines)


def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = [
        int((w / total_spent) * 100) // 10 * 10
        for w in withdrawals
    ]

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for pct in percentages:
            chart += " o " if pct >= level else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    maxlen = max(len(name) for name in names)

    for i in range(maxlen):
        chart += "     "
        for name in names:
            chart += (name[i] + "  ") if i < len(name) else "   "
        if i < maxlen - 1:
            chart += "\n"

    return chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.deposit(1000, "deposit")
clothing.withdraw(340, "trousers")
food.transfer(50, clothing)
print(food)
print(clothing)
print(create_spend_chart([food, clothing]))

