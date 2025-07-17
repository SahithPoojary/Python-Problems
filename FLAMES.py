boy=input("Enter boy name:")
girl=input("Enter girl name:")
girl2=input("Enter girl name:")
a1=list(boy)
a2=list(girl)
a3=list(girl2)
for i in range(len(a1)):
    for j in range(len(a2)):
        for k in range(len(a3)):
            if(a1[i]==a2[j] and a2[j]==a3[k]):
                a1[i]='2'
                a2[j]='2'
                a3[k]='2'
            
# print(a1)
# print(a2)
# print(a3)


for i in a1:
    if (i=='2'):
        a1.remove(i)
for i in a2:
    if (i=='2'):
        a2.remove(i)
num=len(a1)+len(a2)
print(num)


print(num)
ans=['F','L','A','M','E','S']
index=0
while(len(ans!=1)):
    index=(index + (num-1))%len(ans)
    ans.pop(index)
print("The relation is",ans[0])