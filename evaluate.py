def prefix(sentence):
    prf = []
    op = []
    i = 0
    
    while i < len(sentence):
        if sentence[i].isdigit():
            val = 0
            while i < len(sentence) and sentence[i].isdigit():
                val = (val*10) + int(sentence[i])
                i+=1
            prf.append(val)
            if len(op) > 0:
                prf.append(op.pop())
            i-=1
        elif sentence[i] == '+' or sentence[i]=='-':
            op.append(sentence[i])
        i+=1
    while len(op) > 0:
        prf.append(op.pop())
    return prf

def evaluate(sentence):
    prf = prefix(sentence)
    num = []
    i=0
    try:
        while len(prf) > 0:
            tmp = prf.pop(0)
            if type(tmp) is int:
                num.append(tmp)
            elif tmp == '+':
                num1, num2 = num.pop(), num.pop()
                num.append(num1+num2)
            elif tmp == '-':
                num1, num2 = num.pop(), num.pop()
                num.append(num1-num2)
    except:
        raise Exception("Can't evalute this string") from None

    return num[0]
        
