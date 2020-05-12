# CALCULATOR USING EVAL METHOD.

def init():
    operation = input('Please, enter the operation in the next input: ')
    if (len(operation) == 0):
        return print('#Error 001: El campo está vacio.')
    total = eval(operation)
    print(f'Total: {total}')

# loop the constructor: init
while True:
    init()