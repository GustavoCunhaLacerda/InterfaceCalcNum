import sys
import matplotlib.pyplot as plt
import numpy as np

def bissecao(f, ai, bi, erro=1e-3, iteracoes=100):
    '''
        -> retorna uma raíz para a função de acordo com os requisitos pelo método de Bisseção

        f    : funcao analisada
        ai,bi: intervalos inciais de análise do método
        erro : erro para o critério de parada do método
        iteracoes : número máximo de iterações
    '''

    # copia dos valores ai,bi iniciais para uso futuro
    a = ai
    b = bi

    for i in range(iteracoes):
        raiz_aproximada = (a+b)/2
        
        if f(raiz_aproximada)*f(a) > 0:
            a = raiz_aproximada
        else:
            b = raiz_aproximada

        if abs(f(raiz_aproximada)) <= erro:
            break

    return raiz_aproximada

## grafico ##
def grafico_bissecao(f, a, b, raiz_aproximada, f_text):

    x = np.linspace(a, b, 100)
    y = [f(a) for a in x]

    plt.figure(num='Gráfico Bisseção')
    plt.axhline(y=0, color='black', lw = 0.3)
    plt.axvline(x=0, color='black', lw = 0.3)

    plt.plot(x, y, label = "f(x) = {}".format(f_text.replace('**', '^').replace('*', '')))
    plt.plot(raiz_aproximada, f(raiz_aproximada), "ro" , color = "purple",label = "x = {}".format(raiz_aproximada))
    plt.legend()

    
