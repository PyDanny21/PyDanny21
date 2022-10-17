#define functions,add,subtract,multiply,divide

def add(a,b):
    answer=a+b
    print(str(a)+' + '+str(b)+' = '+str(answer))
    return answer
def subtract(a,b):
    answer=a-b
    print(str(a)+' - '+str(b)+' = '+str(answer))
    return answer
def multiply(a,b):
    answer=a*b
    print(str(a)+' X '+str(b)+' = '+str(answer))
    return answer
def divide(a,b):
    answer=a/b
    print(str(a)+' / '+str(b)+' = '+str(answer))
    return answer

while(True):
    a=int(input('Enter number 1:'))
    b=int(input('Enter number 2:'))
    opt=str(input('Enter operation:'))
    if '+' in opt:
        add(a,b)
    elif '-' in opt:
        subtract(a,b)
    elif '*' in opt:
        multiply(a,b)
    elif '/' in opt:
        divide(a,b)

