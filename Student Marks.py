import time
names=[]
marks=[]
for i in range(5):
    n=input("Enter the Name:")
    names.append(n)
    student=[]
    for j in range(3):
        m=int(input("Enter mark{}:".format(j+1)))
        student.append(m)
    marks.append(student)
    
per=[]
for i in marks:
    res=sum(i)//3
    per.append(res)
    
time.sleep(3)
print("-----------------------")
for i in range(5):
    print("{}.{} : {}%".format(i+1,names[i],per[i]))
    
    
    
    
    # 412