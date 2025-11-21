from datetime import date
import pandas as pd
import csv

class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.load()
    
    def load(self, filename="expenses.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expense= self.Expense(self,
                                          description=row["Description"],
                        amount=int(row["Amount"])
                    )
        except FileNotFoundError:
            "File not found, starting with an empty expense list."
            return

        for item in data:
            expense = self.Expense(
                self,
                description=item["Description"],
                amount= item["Amount"]
            )
            expense.date = item["Date"]
            expense.id = item["ID"]
            self.expenses.append(expense)

    def save(self, filename="expenses.csv"):
        try:
            with open(filename, "w+") as file:
                for expense in self.expenses:
                    file.write(f"{expense.id},{expense.description},{expense.amount},{expense.date}\n")

        except FileNotFoundError as err:
           raise(f"File not Found: {err}")
    
    def generate_id(self):
        return len(self.expenses) + 1 if self.expenses else 1

    def add(self, description, amount):
        new_expense = self.Expense(self, description, amount)
        self.expenses.append(new_expense)
        return f"Expense with ID {new_expense.id} added successfully"

    def list(self):
        listed = []
        for expense in self.expenses:
            listed.append(expense.to_dict())

        return pd.DataFrame(listed,
                            columns=["ID", "Description", "Amount", "Date"])

    def update(self, id, description=None, amount=None):
        expense = self.expenses[id - 1]
        if description != None:
            expense.description = description
        if amount != None:
            expense.amount = amount

        self.save()
        return f"Expense with ID {id} updated successfully"

    def delete(self, id):
        if id > len(self.expenses) or id <= 0:
            return f"Expense with given ID {id} does not exist"

        for i in range(len(self.expenses) - 1):
            if self.expenses[i].id == id:
                self.expenses.pop(i)
                for j in range(i, len(self.expenses)):
                    self.expenses[j].id -= 1
        self.save()
        return "Expense removed successfully"

    def summary(self):
        sum = 0
        for expense in self.expenses:
            sum += expense.amount

        return f"Total expenses {sum}"

    def summary_by_month(self, month):
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: " April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        filtered_expenses = [
            expense for expense in self.expenses if expense.date.month == month
        ]
        sum = 0
        for expense in filtered_expenses:
            sum += expense.amount

        return f"Total expenses in {months[month]}: {sum}"

    class Expense:

        def __init__(self, expense_manager, description: str, amount: int):
            self.manager = expense_manager
            self.id = self.manager.generate_id()
            self.description = description
            self.amount = amount
            self.date = date.today()

        def to_dict(self):
            return {
                "ID": self.id,
                "Description": self.description,
                "Date": self.date,
                "Amount": self.amount
            }

if __name__ == "__main__":
    manager = ExpenseManager()
    print(manager.add("Groceries", 150))
    print(manager.add("Transport", 50))
    print(manager.list())
    print(manager.summary())
    print(manager.summary_by_month(6))
