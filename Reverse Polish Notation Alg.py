def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in "*/+-":
            stack.append(int(token))
            continue
        number2 = stack.pop()
        number1 = stack.pop()
        if token == "+":
            result = number2+number1
        elif token == "-":
            result = number1 - number2
        elif token == "*":
            result = number1*number2
        elif token == "/":
            result = int(number1/number2)
        stack.append(result)
    
    return print(stack.pop())

evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

https://leetcode.com/studyplan/leetcode-75/