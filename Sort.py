students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]
per=0
sum1=0
for i in students:
    sum1=sum(i["marks"])
    per=sum1//3
    i["Per"]=per

b=sorted(students ,key=lambda x:x["Per"],reverse=True)
des=["First","Second","Third","Fourth","Fifth"]
index=1
for i in b:
    print("{}.{} stands {} with {}%".format(index,i["name"],des[index-1],i["Per"]))
    index+=1