def FatorialIterativo(n):
    if n < 0:
        print('Erro: n não pode ser negativo')
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def Euler():
    e = 0
    for n in range(999):  
        e += 1 / FatorialIterativo(n)
    return e


print(Euler())
