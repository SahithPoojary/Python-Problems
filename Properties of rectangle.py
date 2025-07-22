# properties of rectangle
# -------------------------
# sum of angle is 360
# each angle is 90
# -------------------------
#Enter len of rectang;e :20
#enter breath of rectangle :30
#area of rectangle is 600
#Perimeter is 100
# --------------------------
#Enter len of rectang;e :20
#enter breath of rectangle :30
#area of rectangle is 600
#Perimeter is 100


class Shape:
    def set_rectangle(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_properties(self):
        print("Sum of angles is 360")
        print("Each angle is 90")

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        self.print_properties()
        print("Length of rectangle:", self.length)
        print("Breadth of rectangle:", self.breadth)
        print("Area of rectangle is:", self.area())
        print("Perimeter is:", self.perimeter())

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

r1 = Shape()
r1.set_rectangle(length, breadth)
r1.display()

# class rect:
#     def get_info(self):
#         a=int(input("Enter the len of rect: "))
#         b=int(input("Enter the breath of rect: "))
#         self.len = a
#         self.breath = b
#     def area(self):
#         print(self.len*self.breath)

# print("The Rectangle Properties")
# print(rect.prop1)
# print(rect.prop2)
# a1=rect()
# a2=rect()
# a1.get_info()
# a2.get_info()
# a1.area()
# a2.area()

#   ++++     ++++
#  ++++++   ++++++
# ++++++++ ++++++++
#  +++++++++++++++
#   +++++++++++++
#    +++++++++++
#     +++++++++
#      +++++++
#       +++++
#        +++
#         +



