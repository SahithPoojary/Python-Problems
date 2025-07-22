class LC37:
    def student(self, name):
        self.name=name
    def display(self):
        self.nature() #calling nature inside the method
        print("The name is ", format(self.name))
    def nature(self):
        print("Hello guyssss.......")

a1=LC37()
a1.student("Sahith Poojary")
a1.display()