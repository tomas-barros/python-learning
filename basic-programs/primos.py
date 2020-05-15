def esPrimo(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x == 0:
            return False
    return True

while True:
    inp = int(input('Type the number: '))
    if (esPrimo(inp)):
        print(f"{inp} es primo.")
    else:
        print(f'{inp} no es primo.')