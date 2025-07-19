# dict= {"A":1 ,"B":10,"C":100,"D":1000,"E":10000,"F":100000}
# ip="A"
# res=0
# for i in ip:
#     if (i in dict):


# num = int(input("Enter the number....:"))
# def gcd(a,b):
#     while(b!=0):
#         temp=a%b
#         a=b
#         b=temp
#     return a

# def cop(a,b):
#     return gcd(a,b)==1

# for i in range(1,num):
#     for j in range(1,i):
#         for k in range(1,j):
#             if (j*j + k*k == i*i and cop(i,j) and cop(j,k) and cop(i,k)):
#                 print(k,j,i)

# 3D Prime
# 1)number should be a Prime
# 2) 3 digit
# 3)sum of digit --> prime
# 4) every digit --> prime

# def prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# prime_digits = {'2', '3', '5', '7'}
# print("3 digit prime numbers are....:")

# for num in range(100, 1000):
#     if not prime(num):
#         continue
#     digits = list(str(num))
#     if not all(d in prime_digits for d in digits):
#         continue
#     digit_sum = sum(int(d) for d in digits)
#     if not prime(digit_sum):
#         continue
#     print(num)

def prime(i):
    if(i==1):
        return False
    else:
        for j in range(2,i):
            if(i%j==0):
                return False
        return True
def sod(i):
    d = list(str(i))
    x=sum([int(i for i in d)])
    if (prime(x)):
        return True
    else:
        return False

def dig(i):
    
    while(i>0):
        d=i%10
        d=i//10
        if (prime(d)):
            return False
        i=i//10
        