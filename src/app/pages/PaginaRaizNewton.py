import time
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import ttk
from methods.str_para_funcao import *
from methods.raizes.newton import *

FONTE = ("Verdana", 12)
FONTE_TEXTO =  ("Verdana", 15)
FONTE_TITULO = ("Verdana", 15, "bold")

BUTTON_WIDTH = 40
BUTTON_FILL = "y"

BG_COLOR = "#1A5276"


class PaginaRaizNewton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self,
            text = "RAÍZ NEWTON",
            font = FONTE_TITULO,
            foreground = "white",
            bg = BG_COLOR,
            heigh = 4
        )
        title_label.pack(side = "top", fill = "x")
    #---------------- input funcao e derivada da funcao -----------------#
        func_container = tk.Label(self)
        func_container.pack(side = "top", pady = (10, 0))
        
        diff_func_container = tk.Label(self)
        diff_func_container.pack(side = "top")

        func_text = tk.Label(
            func_container,
            text = "F (x):"
        ).pack(side = "left")

        self.func_entry = tk.Entry(
            func_container,
            width = BUTTON_WIDTH
        )
        self.func_entry.pack(side = "right")

        diff_func_text = tk.Label(
            diff_func_container,
            text = "F'(x):"
        ).pack(side = "left")

        self.diff_func_entry = tk.Entry(
            diff_func_container,
            width = BUTTON_WIDTH
        )
        self.diff_func_entry.pack(side = "right")


        #------------- ponto inicial ----------------#
        xi_label = tk.Label(self)
        xi_label.pack(side = "top", pady = 5)
        ##

        xi_text = tk.Label(
            xi_label,
            text = "Ponto Inicial (xi):"
        ).pack(side = "left")

        self.xi_entry = tk.Entry(
            xi_label,
            width = 10
        )
        self.xi_entry.pack(side = "left", padx = 20)


        #------------ erro e iteracoes maximas -------------#
        erro_it_label = tk.Label(self)
        erro_it_label.pack(side = "top")

        ##
        self.erro_combobox = ttk.Combobox(
            self,
            width = 40,
            values = ["Erro (Padrão = 10e-3)", "10e-1", "10e-2", "10e-3", "10e-4", "10e-5"]
        )
        self.erro_combobox.current(0) 
        self.erro_combobox.pack(side = "top", fill = BUTTON_FILL)

        self.iteracoes_combobox = ttk.Combobox(
            self,
            width = 40,
            values = ["Max. de Iterações (Padrão = 100)", "5", "10", "100", "1000", "10000"]
        )
        self.iteracoes_combobox.current(0) 
        self.iteracoes_combobox.pack(side = "top", fill = BUTTON_FILL)

        #----------------- grafico (y/n) -------------------#
        self.graph = tk.IntVar()
        graph_radio = tk.Checkbutton(self, text = "Plotar Gráfico", variable = self.graph)
        graph_radio.pack(side = "top", pady = (10, 0))
        graph_radio.var = self.graph

        #----------------- botao calcular ------------------#
        calcular_button = tk.Button(
            self,
            text = "Calcular",
            bg = "white",
            width = BUTTON_WIDTH,
            command = self.calcular_raiz_newton
        )
        calcular_button.pack(side = "top", fill = BUTTON_FILL, pady = 10)

        #----------------- resultado -----------------------#
        self.resultado_raiz = tk.Label(
            self,
            text = "Raiz:\n"
        ) 
        self.resultado_raiz.pack(side = "top", fill = BUTTON_FILL, pady = 10)
        
        self.resultado_time = tk.Label(
            self,
            text = "Tempo de execução:\n"
        ) 
        self.resultado_time.pack(side = "top", fill = BUTTON_FILL, pady = 10)

        margin_label = tk.Label(self, bg = BG_COLOR)
        margin_label.pack(side = "bottom", fill = "x", pady = (10, 0))

    def calcular_raiz_newton(self):
        f = self.func_entry.get()
        f = expressao_generica(f)

        df = self.diff_func_entry.get()
        df = expressao_generica(df)
        
        xi = int(self.xi_entry.get())

        erro = self.erro_combobox.get()
        if erro[0] != "E":
            erro = float(erro)
        else:
            erro = 10e-3

        iteracoes = self.iteracoes_combobox.get()
        if iteracoes[0] != "M":
            iteracoes = int(iteracoes)
        else:
            iteracoes = 100
        
        inicio = time.time()
        raiz = raiz_newton(f.f, df.f, xi, erro = erro, iteracoes = iteracoes)
        fim = time.time()
        self.resultado_raiz["text"] = "Raiz:\n{}".format(raiz)

        self.resultado_time["text"] = "Tempo de execução:\n{}".format(fim - inicio)
        self.update_idletasks()

        # plot do grafico #
        if self.graph.get() == 1:
            grafico_raiz_newton(f.f, xi, raiz, self.func_entry.get())
            plt.show()
