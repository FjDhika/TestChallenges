from functools import cmp_to_key

def larg(num1, num2):
    if str(num1)+str(num2) < str(num2)+str(num1):
        return 1
    elif str(num1)+str(num2) == str(num2)+str(num1):
        return 0
    else:
        return -1

def largest(numbers):
    x = sorted(numbers, key=cmp_to_key(larg))
    x = [str(itm) for itm in x]
    return ''.join(x)
