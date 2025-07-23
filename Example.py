# # /////////OOP's CONSEPT/////////


# class LC37:
#     def student(self, name):
#         self.name=name
#     def display(self):
#         self.nature() #calling nature inside the method
#         print("The name is ", format(self.name))
#     def nature(self):
#         print("Hello guyssss.......")

# a1=LC37()
# a1.student("Sahith Poojary")
# a1.display()


#2)-----------------------------------------------
###PASS FAIL////////////

# class college:
#     col="NITTE"
#     def student(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def passfail(self):
#         if(self.mark>40):
#             print("PASS")
#         else:
#             print("Fail")
#     def modify(self,grace):
#         self.mark=self.mark+grace
#     def display(self):
#         print("Name: ",self.name)
#         print("College: ",self.col)
#         print("Mark: ",self.mark)
#         self.passfail()

# s1=college()
# s2=college()
# s1.student("SAHIITH",59)
# s2.student("SAMPREETH",60)
# s1.display()
# print("---------------------------------")
# s2.display()

# # 2 b) TO PRINT NITTE ONLY/////////
# class college:
#     col="NITTE"
#     def student(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def passfail(self):
#         if(self.mark>40):
#             print("PASS")
#         else:
#             print("Fail")
#     def modify(self,grace):
#         self.mark=self.mark+grace
#     def display(self):
#         print("Name: ",self.name)
#         print("College: ",self.col)
#         print("Mark: ",self.mark)
#         self.passfail()
# print(college.col)



#==================================================

class india:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("The name is", self.name)

    def nature(self):
        print("{} is good player".format(self.name))
        
a1=india("Sampreeth")
a1=india("Sahith")
a1.display()
a1.display()
