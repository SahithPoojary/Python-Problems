from tabulate import tabulate
headers = ["Names","Age","Department"]
data=[
    ["Ravi",25,"HR"],
    ["Anjali",30,"Finance"],
    ["Mohan",28,"IT"],
    ["Sneha",24,"Marketing"],
    ["Sunish",27,"Bussiness"]
]
print(f"{headers[0]:<12}{headers[1]:<5}{headers[2]:<15}")
print("*" *30)

for row in data:
    print(f"{row[0]:<12}{row[1]:<5}{row[2]:<15}")
    print("-"*30)