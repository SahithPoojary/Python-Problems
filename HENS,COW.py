
heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))
flag=False
for hen in range(heads):
    cows = heads - hen
    if(cows*4+hen*2==legs):
        print("COWS:",cows)
        print("HENS:",hen)
        flag=True
        break
if(not flag):
    print("No solution exists")