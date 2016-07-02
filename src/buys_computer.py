class PossibleCustomer:
    def __init__(self, age, income, student, credit_rating):
        self.age = age
        self.income = income
        self.student = student
        self.credit_rating = credit_rating
        self.buys_computer = None
    def set_buys_computer(self, buys):
        self.buys_computer = buys


possible_customers = [
    PossibleCustomer(30, "Medium", False, "Excellent"), # 15
    PossibleCustomer(30, "Low", False, "Fair"), # 16
    PossibleCustomer(30, "Low", False, "Excellent"), #17
    PossibleCustomer(31, "Low", True, "Fair"), # 18
    PossibleCustomer(41, "Medium", True, "Excellent"), # 19
    PossibleCustomer(31, "High", False, "Excellent"),
]

for elem in possible_customers:
    if elem.age >= 31 and elem.age <= 40:
        elem.set_buys_computer(True)
    elif elem.age <= 30:
        if elem.student:
            elem.set_buys_computer(True)
        else:
            elem.set_buys_computer(False)
    else: # age > 40
        if elem.credit_rating == "Fair":
            elem.set_buys_computer(True)
        elif elem.credit_rating == "Excellent":
            elem.set_buys_computer(False)
        else:
            raise ValueError("Unknown credit rating!")

for elem in possible_customers:
    print(elem.buys_computer)

