import sys
import matplotlib.pyplot as plt
import numpy as np

def raiz_newton(f, df, xi, erro = 10e-3, iteracoes = 100):
    '''
        -> retorna uma raíz para a função de acordo com os requisitos pelo método de Newton

        f    : função analisada
        df   : derivada da função analisada
        ai,bi: intervalos inciais de análise do método
        erro : erro para o critério de parada do método
        iteracoes : número máximo de iterações  
    '''

    xBarra = [xi]    # Aproximação inicial de x

    for i in range(1, iteracoes):
        # Atualização da aproximação da raíz
        x = xBarra[i-1] - (f(xBarra[i-1])/df(xBarra[i-1]))
        xBarra.append(x)

        # Ponto de precisão determinado
        if abs(f(x)) < erro:
            break
    
    return x

def grafico_raiz_newton(f, xi, raiz_aproximada, f_text):
    '''
        f      : funcao analisada
        f_text : string da funcao
        ai,bi  : intervalos inciais de analise do metodo
        raiz_aproximada : raiz encontrada pelo metodo
    '''
    a = int(xi - abs((2*raiz_aproximada))  - xi)
    b = int(xi + abs((2*raiz_aproximada))  + xi)
    
    x = np.linspace(max(a,b), min(a,b), 100)
    y = [f(a) for a in x]

    plt.figure(num='Gráfico Raíz Newton')
    plt.axhline(y=0, color='black', lw = 0.3)
    plt.axvline(x=0, color='black', lw = 0.3)

    plt.plot(x, y, label = "f(x) = {}".format(f_text.replace('**', '^').replace('*', '')))
    plt.plot(xi, f(xi), "ro" , color = "blue",label = "xi = {}".format(xi))
    plt.plot(raiz_aproximada, f(raiz_aproximada), "ro" , color = "purple",label = "x = {}".format(raiz_aproximada))
    plt.legend()
