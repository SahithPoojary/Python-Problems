def cal(x, a, b):
    if a >= x:
        return 1
    if a <= b:
        return -1
    n = ((x - a) + (a - b) - 1) // (a - b) + 1  
    return n

cal(30,10,5)
result = cal(x, a, b)
if result == -1:
    print("Monkey will never reach the top.")
else:
    print(f"Minimum time required: {result} minutes")