import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from functools import reduce
x = Symbol('x')

def interpolar_mmq(x_vet, y_vet, grau):
    '''
        -> retorna uma string do polinômio resultante da interpolação de Mínimos Quadrados

        x_vet : dados de x já conhecidos da função 
        y_vet : dados de f(x)/y já conhecidos da função 
        grau  : grau desejado para o polinômio resultante
    '''

    x_vet = np.array(x_vet)
    y_vet = np.array(y_vet)
    n = len(x_vet)
    pot = 2*grau

    # verificaçao da entrada
    if len(x_vet) != len(y_vet): 
        return "ERRO! Quantidade de informações x e y diferentes"

    ## matriz * coef = fs ##
    # formando a matriz
    matriz = []
    for i in range(grau+1):
        linha = []
        for j in range(grau+1):
            if i == j == grau:
                linha.append(n)
            else:
                linha.append(np.sum(x_vet**(pot-j)))
        matriz.append(linha)
        pot -= 1
    
    # formando fs #
    fs = []
    for i in range(grau+1):
        fs.append(np.sum(y_vet*x_vet**(grau-i)))

    # resoluçao do sistema linear -> matriz * coef = fs #
    coef = np.linalg.solve(matriz, fs)
    
    # formação do polinômio
    poli_temp = []
    for i in range(len(coef)):
        poli_temp.append(round(coef[i], 3)*x**(grau - i))

    poly = reduce(lambda a,b : a+b, poli_temp)

    return str(poly)



# grafico do polinomio 
def grafico_interpolar_mmq(f, x_vet, y_vet, f_text):
    
    x = np.linspace(min(x_vet), max(x_vet), 100)
    y = [f(a) for a in x]

    plt.figure(num='Gráfico Interpolação Mínimos Quadrados')
    plt.axhline(y=0, color='black', lw = 0.3)
    plt.axvline(x=0, color='black', lw = 0.3)

    plt.plot(x, y, label = "f(x) = {}".format(f_text.replace('**', '^').replace('*', '')))
    plt.plot(x_vet, y_vet, "ro" , color = "purple",label = "x[] && y[]")
    plt.legend()