names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
memo = [0, 1, 1, 1, 2, 2, 1, 2, 1, 2]
salary = [1000, 2000, 3000, 4500, 2000, 5000, 1500, 2300, 1300, 1100]

data = list(zip(salary, memo, names))

removed1 = []
removed2 = []

for i in data:
    if i[0] > 4000:
        removed1.append(i)

remaining = [i for i in data if i[0] <= 4000]
a = sorted(remaining, key=lambda x: x[0], reverse=True)

for i in a:
    if i[1] >= 2:
        removed2.append(i)
    if len(removed2) >= 3:
        break

final = removed1 + removed2

index = 0
for i in final:
    print("{},{} : Memo {} : Salary {}".format(index, i[2], i[1], i[0]))
    index += 1
