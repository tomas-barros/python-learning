def makefibonacciSuccesion(quantity):
    numbers = []
    total = 0
    total_a = 1
    total_b = 0
    for _ in range(quantity):
        total = total_a + total_b
        total_b = total_a
        total_a = total
        numbers.append(total)
    print (numbers)

while True:
    inp = int(input('Please, type the range of numebers: '))
    makefibonacciSuccesion(inp)