class emp:
    profit = 1000000
    tax = 10
    company = "TCS"

    def __init__(self, name, sal, age, per):
        self.name = name
        self.age = age
        self.sal = sal
        self.per = per
        self.tax = emp.tax
        self.profit = emp.profit

    def cal_tax(self):
        return ((emp.tax / 100) * self.sal)

    def cal_share(self):
        return ((self.per / 100) * emp.profit)

    def display(self):
        print("1.", self.name)
        print("2.", emp.company)
        print("3.", self.age)
        print("4.", self.sal)
        print("5.", self.cal_tax())
        print("6.", self.cal_share())

a1 = emp("Amit", 50000, 30, 10)
a2 = emp("Ravi", 60000, 28, 15)
a3 = emp("Sita", 70000, 25, 20)

a1.display()
print("**********")
a2.display()
print("**********")
a3.display()
