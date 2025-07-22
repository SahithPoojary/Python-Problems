# class rect:
#     def set_dim(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
#     def display(self):
#         self.print_properties()
#         print("Length of rectangle:", self.length)
#         print("Breadth of rectangle:", self.breadth)


# num=[]
# d=int(input("Enter the number of rectangles: "))
# for i in range(d):
#     length = int(input("Enter length of rectangle : "))
#     breadth = int(input("Enter breadth of rectangle : "))
#     r = rect()
#     r.set_dim(length, breadth)
#     num.append(r)

# iii=1
# for i in num:
#     print("Area of a Rectangle {} is:{}".format(iii, i.area()))
#     iii+=1



class rect:
    def set_dim(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth


num=[]
d=int(input("Enter the number of rectangles: "))
for i in range(d):
    r = rect(i+10, i+20)
    num.append(r)


for i in num:
    print(i.a)


