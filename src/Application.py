import sys

application_path = sys.path[0] 
sys.path.append(application_path+'/app/')
sys.path.append(application_path+'/app/pages/')
sys.path.append(application_path+'/app/methods/')
sys.path.append(application_path+'/app/methods/integracao')
sys.path.append(application_path+'/app/methods/interp')
sys.path.append(application_path+'/app/methods/raizes')

import tkinter as tk

from PaginaPrincipal import *
from PaginaSobre import *
from PaginaTutorial import *
from PaginaBissecao import *
from PaginaRaizNewton import *
from PaginaInterpNewton import *
from PaginaInterpMMQ import *
from PaginaIntegracaoTrap import *
from PaginaIntegracaoSimp import *

LARGURA_JANELA = "600" 
ALTURA_JANELA  = "500"

PAGES = (
    PaginaInicial,
    PaginaSobre,
    PaginaTutorial,
    PaginaBissecao,
    PaginaRaizNewton,
    PaginaInterpNewton,
    PaginaInterpMMQ,
    PaginaIntegracaoTrap,
    PaginaIntegracaoSimp,
)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # heranca de Tk

        #--------- configs do container principal -----------------#
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        #--------- dicionario de classes de paginas -----------------#
        self.frames = {}
        for P in PAGES:
            frame = P(container, self)
            self.frames[P] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # mostra a tela inicial na abertura
        self.show_frame(PaginaInicial)


        #--------- menu de transicoes do topo (barra de menu) -----------------#
        menu_bar = tk.Menu(self)
        self.config(menu = menu_bar)

        menu_bar.add_command(label='Inicio'  , command = lambda: self.show_frame(PaginaInicial))
        menu_bar.add_command(label='Tutorial', command = lambda: self.show_frame(PaginaTutorial))
        menu_bar.add_command(label='Sobre'   , command = lambda: self.show_frame(PaginaSobre))
        menu_bar.add_command(label='Histórico')

    # metodo para mostrar a pag desejada
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.title("Ambiente Gráfico Cálculo Numérico")
    app.geometry(LARGURA_JANELA+"x"+ALTURA_JANELA)
    app.mainloop()
