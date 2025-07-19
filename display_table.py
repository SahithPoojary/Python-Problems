import tabulate
headers = ["Names","Age","Department"]
data=[
    ["Ravi",25,"HR"],
    ["Anjali",30,"Finance"],
    ["Mohan",28,"IT"],
    ["Sneha",24,"Marketing"],
    [" Aastha Sunish",27,"Bussiness"]
]
print(tabulate(data,headers=headers, tablefmt="fancy_grid"))