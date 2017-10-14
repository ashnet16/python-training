'''This module allows us to converts infix to postfix and perform postfix operations.'''
from stack import Stack


def converter(string):
    '''This function converts a infix to postfix. '''
    string_list = string.split()
    print string_list
    pres = {'(':1, '+':2, '-':2, '*':3, '/':3, '**':4}
    output = []
    opstack = Stack()
    for item in string_list:
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or item in "0123456789":
            output.append(item)
        elif item == '(':
            test = opstack.push(item)
        elif item == ')':
            test = opstack.peek()
            opstack.pop()
            while test != '(':
                output.append(test)
                test = opstack.peek()
                opstack.pop()
        else:
            while (not opstack.is_empty()) and (pres[opstack.peek()] >= pres[item]):
                output.append(opstack.peek())
                opstack.pop()
            opstack.push(item)
    while not opstack.is_empty():
        output.append(opstack.peek())
        opstack.pop()
    return ''.join(output)

def evaluator(string):
    '''This function will evaluate the math operations as provided by the postfix.'''
    string_list = string.split()
    pres = ['+', '-', '*', '/']
    operand = Stack()
    for item in string_list:
        if item not in pres:
            operand.push(int(item))
        else:
            afirst = operand.peek()
            operand.pop()
            bsecond = operand.peek()
            operand.pop()
            result = operate(bsecond, item, afirst)
            operand.push(result)
    return operand.peek()
def operate(operand1, operator, operand2):
    '''This function performs the math operations passed in as parameters.'''
    if operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1/operand2
    elif operator == '+':
        return operand1+operand2
    elif operator == '-':
        return operand1-operand2
    else:
        raise Exception('Operation not supported')
    