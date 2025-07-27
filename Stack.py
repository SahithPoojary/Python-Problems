def find(exp):
    operand = []
    operator = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    i = 0

    while i < len(exp):
        if exp[i].isdigit():
            nums = ""
            while i < len(exp) and exp[i].isdigit():
                nums += exp[i]
                i += 1
            operand.append(int(nums))
        else:
            while operator and priority.get(operator[-1], 0) >= priority.get(exp[i], 0):
                op = operator.pop()
                num2 = operand.pop()
                num1 = operand.pop()
                if op == '+':
                    operand.append(num1 + num2)
                elif op == '-':
                    operand.append(num1 - num2)
                elif op == '*':
                    operand.append(num1 * num2)
                elif op == '/':
                    operand.append(num1 // num2)
            operator.append(exp[i])
            i += 1

    while operator:
        op = operator.pop()
        num2 = operand.pop()
        num1 = operand.pop()
        if op == '+':
            operand.append(num1 + num2)
        elif op == '-':
            operand.append(num1 - num2)
        elif op == '*':
            operand.append(num1 * num2)
        elif op == '/':
            operand.append(num1 // num2)

    return operand[0]
exp = "10+2*3/4+3"
res = find(exp)
print(res)