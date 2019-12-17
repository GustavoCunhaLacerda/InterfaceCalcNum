import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from functools import reduce
x = Symbol('x')

'''
    Créditos do código de Interp de Newton ao Luiz Gustavo Benicio Neves
    Disponível 'livremente' em : 
    https://github.com/LouisRiverstone/CalculoNumerico/blob/master/Polinomios%20de%20Interpolacao/Newtao.py
'''

## funcao das diferenças divididas
def diferencasDivididas(vet):
    '''
        -> retorna os valores necessários da tabela de diferenças divididas de Newton

        vet : aglomerado de x com f(x)/y correspondente [[x1, y1], [x2, y2], ..., [xn, yn]]
    '''
    val = []
    count = 0
    
    vetdelta = [vet[i][1] for i in range(len(vet))]
    vetx = [vet[i][0] for i in range(len(vet))]
    
    while (len(vetdelta) > 1):

        vettemp = []
        val.append(vetdelta[0])
        count+=1

        for i in range(len(vetdelta) - 1):
            temp = (vetdelta[i + 1] - vetdelta[i]) / (vetx[i + count] - vetx[i])
            vettemp.append(temp)
        vetdelta = vettemp

    val.append(vetdelta[0])

    return val

## funçao do calc do polinomio de newton 
def calc_interp_newton(x_vet, y_vet):
    '''
        -> retorna uma string do polinômio resultante da interpolação de Newton

        x_vet : dados de x já conhecidos da função 
        y_vet : dados de f(x)/y já conhecidos da função 
    '''

    # verificaçao da entrada
    if len(x_vet) != len(y_vet): 
        return "ERRO! Quantidade de informações x e y diferentes"

    vet = [[x_vet[i], y_vet[i]] for i in range(len(x_vet))]

    val = diferencasDivididas(vet)

    funcfinal = []
    funcfinal.append(val[0])

    for i in range(1,len(vet)):
        functemp = []
        for j in range(i):
            functemp.append(x - vet[j][0])
        funcfinal.append(round(val[i], 3) * reduce(lambda x, y: x * y,functemp))

    polinomio = simplify(reduce(lambda x,y:x + y,funcfinal))
    
    return str(polinomio)


# grafico do polinomio 
def grafico_calc_interp_newton(f, x_vet, y_vet, f_text):
    
    xv = np.linspace(min(x_vet), max(x_vet), 100)
    yv = [f(a) for a in xv]

    plt.figure(num='Gráfico Interpolação Newton')
    plt.axhline(y=0, color='black', lw = 0.3)
    plt.axvline(x=0, color='black', lw = 0.3)

    plt.plot(xv, yv, label = "f(x) = {}".format(f_text.replace('**', '^').replace('*', '')))
    plt.plot(x_vet, y_vet, "ro" , color = "purple",label = "x[] && y[]")
    plt.legend()