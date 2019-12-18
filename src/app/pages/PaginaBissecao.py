import time
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import ttk
from methods.str_para_funcao import *
from methods.raizes.bissecao import *

FONTE = ("Verdana", 12)
FONTE_TEXTO =  ("Verdana", 15)
FONTE_TITULO = ("Verdana", 15, "bold")

BUTTON_WIDTH = 40
BUTTON_FILL = "y"

BG_COLOR = "#1A5276"

class PaginaBissecao(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self,
            text = "BISSEÇÃO",
            font = FONTE_TITULO,
            foreground = "white",
            bg = BG_COLOR,
            heigh = 4
        )
        title_label.pack(side = "top", fill = "x")

        #---------------- input funcao -----------------#
        func_container = tk.Label(self)
        func_container.pack(side = "top", pady = 20)
        
        func_text = tk.Label(
            func_container,
            text = "Função:"
        ).pack(side = "left")

        self.func_entry = tk.Entry(
            func_container,
            width = BUTTON_WIDTH
        )
        self.func_entry.pack(side = "right")

        #------------- intervalo [a ,b] ----------------#
        interval_label = tk.Label(self)
        interval_label.pack(side = "top")
        ##

        interval_text = tk.Label(
            interval_label,
            text = "Intervalo [a, b]:"
        ).pack(side = "left")

        self.a_entry = tk.Entry(
            interval_label,
            width = 10
        )
        self.a_entry.pack(side = "left", padx = 20)

        self.b_entry = tk.Entry(
            interval_label,
            width = 10
        )
        self.b_entry.pack(side = "right", fill = BUTTON_FILL)

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
            command = self.calcular_bissecao
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

    def calcular_bissecao(self):
        f = self.func_entry.get()
        f = expressao_generica(f)
        
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())

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
        raiz = bissecao(f.f, a, b, erro = erro, iteracoes = iteracoes)
        fim = time.time()
        self.resultado_raiz["text"] = "Raiz:\n{}".format(raiz)

        self.resultado_time["text"] = "Tempo de execução:\n{}".format(fim - inicio)
        self.update_idletasks()

        # plot do grafico #
        if self.graph.get() == 1:
            grafico_bissecao(f.f, int(a), int(b), raiz, self.func_entry.get())
            plt.show()
