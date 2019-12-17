import numpy as np
import matplotlib.pyplot as plt

# funcao de calculo de integral por regra dos trapezios
def regra_trapezios(f, a, b, pontos):
    '''
        -> retorna o valor da integral pelo método de trapézios

        f  : funçao analisada
        a  : limite inferior de integraçao
        b  : limite superior de integraçao
        pontos : quantidade de pontos formadores de trapézios
    '''

    # Calculando os pontos dos trapézios
    pontosx_t = np.linspace(a, b, pontos) 
    pontosy_t = [f(a) for a in pontosx_t]

    # calculando a area de cada trapezio
    areas_t = []
    for i in range(pontos-1):
        h = np.abs(pontosx_t[i] - pontosx_t[i+1])
        area = (pontosy_t[i]+pontosy_t[i+1])*h/2
        areas_t.append(area)

    return np.sum(areas_t)

## graficos ## 
def grafico_trapezios(f, a, b, pontos, f_text):

    pontosx_t = np.linspace(a, b, pontos) 
    pontosy_t = np.array([float(f(a)) for a in pontosx_t])

    plt.figure(num='Gráfico Integração Trapézios')
    plt.axhline(y=0, color='black', lw = 0.3)
    plt.axvline(x=0, color='black', lw = 0.3)

    x = np.linspace(a-1, b+1, 500)
    y = np.array([float(f(a)) for a in x])

    plt.stem(pontosx_t, pontosy_t, basefmt=' ', markerfmt='', use_line_collection=True, label='Trapezio(s)')
    plt.fill_between(pontosx_t, 0, pontosy_t, label='Area do(s) Trapezio(s)', alpha=0.3)
    plt.plot(x, y, color='#ff4a0c' , linewidth=2.0, label = "f(x) = {}".format(f_text.replace('**', '^').replace('*', '')))
    plt.legend()
