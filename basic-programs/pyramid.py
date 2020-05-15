def makepyramid(width):
    for x in range(width):
        x += 1
        symbol = "*" * x
        print(symbol)

while True:
    makepyramid_inp = int(input("Please, type the width of the half-pyramid: "))
    makepyramid(makepyramid_inp)