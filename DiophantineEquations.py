from math import sqrt
def sol_equa(n):
    sol = []
    for i in range(1, int(sqrt(n))+1):
        if n % i != 0:
            continue

        j = n / i
        y = (j - i) / 4
        x = i + 2 * y
        x = int(x)
        y = int(y)

        if x >= 0 and y >= 0 and (j == x + 2 * y) and (i == x - 2 * y):
            sol.append([x, y])
            
    return sorted(sol, reverse=True)
