    # def load(self, filename="expenses.csv"):
    #     try:
    #         with open(filename, "r") as file:
    #             data = file.read()

    #     except FileNotFoundError as err:
    #        raise(f"File not Found: {err}")

    #     for item in data:
    #         expense = self.Expense(
    #             self,
    #             description=item["Description"],
    #             amount= item["Amount"]
    #         )
    #         expense.date = item["Date"]
    #         expense.id = item["id"]
    #         self.expenses.append(expense)

    # def save(self, filename="expences.csv"):
    #     try:
    #         with open(filename, "w+") as file:
    #             for expense in self.expenses:
    #                 file.write(expense.to_dict())

    #     except FileNotFoundError as err:
    #        raise(f"File not Found: {err}")