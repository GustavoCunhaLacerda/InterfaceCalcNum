import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def regra_simpson(f, a, b, pontos):
    '''
        -> retorna o valor da integral pelo método de simpson

        f  : funçao analisada
        a  : limite inferior de integraçao
        b  : limite superior de integraçao
        pontos : quantidade de pontos formadores da interpolação para regra de simpson
    '''

    pontosx_t = np.linspace(a, b, pontos)
    pontosy_t = np.array([float(f(a)) for a in pontosx_t])

    integral = []
    h = np.abs(pontosx_t[0]-pontosx_t[1])

    for i in range(0, pontos-2, 2):
        soma = (h/3)*(pontosy_t[i] + 4*pontosy_t[i+1] + pontosy_t[i+2])
        integral.append(soma)

    return np.sum(integral)


## graficos ## 
def grafico_simpson(f, a, b, pontos, f_text):

    pontosx_t = np.linspace(a, b, pontos) 
    pontosy_t = np.array([float(f(a)) for a in pontosx_t])

    plt.figure(num='Gráfico Integração Simpson')
    plt.axhline(y=0, color='black', lw = 0.3)
    plt.axvline(x=0, color='black', lw = 0.3)

    x = np.linspace(a-1, b+1, 500)
    y = np.array([float(f(a)) for a in x])

    plt.plot(x, y, color='#ff4a0c' , linewidth=2.0, label = "f(x) = {}".format(f_text.replace('**', '^').replace('*', '')))
    
    for i in range(0, pontos-2, 2):
        pts_x = np.array([pontosx_t[i], pontosx_t[i+1], pontosx_t[i+2]])
        pts_y = np.array([float(f(a)) for a in pts_x])

        f_interp = interp1d(pts_x, pts_y, kind='quadratic')

        x_simp = np.linspace(pts_x[0], pts_x[2], 50)
        y_simp = f_interp(x_simp)

        if i == 0:
            plt.fill_between(x_simp, 0, y_simp, alpha=0.3, label = 'Área de Simpson')
        else:
            plt.fill_between(x_simp, 0, y_simp, alpha=0.3)

        plt.stem(pts_x, pts_y, basefmt=' ', use_line_collection=True)
        plt.plot(x_simp, y_simp)
    
    plt.legend()
