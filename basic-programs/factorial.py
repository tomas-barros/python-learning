def calc_fact(num):
    total = 0
    final_tot = 1
    for x in range(num):
        total = final_tot * (x+1)
        final_tot = total
    print(total)

calc_fact(10) # excepted output: 3628800