#TOWER OF HANOI///////

#1) move n-1 disks from a to b (C is auxi)
#2) move nth disk from a to c (B is auxi)
#3) move n-1 disk from b to c (A is auxi)

def tower(disk,source,auxi,dest):
    if(disk==1):
        print("Move disk 1 from source to destination....")
        return
    else:
        tower(disk-1,source,dest,auxi)
        print("Move {} from {} to {}".format(disk,source,dest))
        tower(disk-1,auxi,dest,source)

disk = int(input("Enter any number"))
print("steps involve are:")
tower(disk,'A','B','C')