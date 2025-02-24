from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:
                return False
    return stack.peek() is None

def no_stack_is_balanced(input_str):
    op = 0
    cp = 0
    for char in input_str:
        if char == "(":
            op += 1
        if char == ")":
            cp += 1
            if cp > op:
                return False
    if cp == op:
        return True
    return False