def evalRPN(tokens: list[str]) -> int:
    math_stack = []
    if len(tokens) == 1:
        operation = int(tokens[0])
        return operation

    ops = {'+': lambda a, b: a + b, '-': lambda a,b:a-b , '*': lambda a,b: a*b, '/': lambda a,b: int(a/b) }
    for item in tokens:
        if item in ['+' , '-' , '*' , '/']:
            b=math_stack.pop()
            a=math_stack.pop()
            # if item == '/':
            #     opertation = int(a)//int(b)
            # else:
            opertation = ops[item](int(a),int(b))
            math_stack.append(opertation)
        else:
            math_stack.append(item) # a number so we add it
    return opertation

# ---- Tests ----
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))  # Expected: 9

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))  # Expected: 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))  # Expected: 22

tokens = ["3","11","5","+","-"]
print(evalRPN(tokens))  # Expected: -13

tokens = ["3"]
print(evalRPN(tokens))  # Expected: 3