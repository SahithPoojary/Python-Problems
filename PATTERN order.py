
# a=int(input("Enter the num of rows:"))
# for i in range(a):
#     for i in range(a-i):
#         print("*",end=" ")
#     print()

a=int(input("Enter the num of rows:"))
for i in range(a):
    for i in range(a-i):
        print("*",end=" ")
    print()
for j in range(a):
    for j in range(j-i):
        print("*",end=" ")
    print()