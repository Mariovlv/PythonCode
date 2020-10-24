import math

def reglaSimpson(a, b, n):
    resultado = 0
    sumatoria = 0
    Delta = ((b-a)/n)
    for i in range(n+1):
        xi = (a + (i*Delta))
        # funcion
        funcion = math.e**(xi**2)
        if xi == a or xi == b:
            sumatoria += funcion
        elif i % 2 != 0:
            funcion = 4*funcion
            sumatoria += funcion
        elif i % 2 == 0:
            funcion = 2*funcion
            sumatoria += funcion
        
    resultado = (Delta/3)*sumatoria

    return resultado
        
print( "El resultado de la integral es:", reglaSimpson(0, 1, 100))