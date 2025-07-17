n=int(input("Enter No. of Teams:"))
teams=[]
for i in range(n):
    a = input("enter team Names:")
    teams.append(a)
meet=int(input("Enter the number of meeting btw one pair:"))

match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append((teams[i],teams[j]))
            
print("------------------------")
index=1
for i in match:
    print("Match{}: {} vs {}".format(index,i[0],i[1]))

