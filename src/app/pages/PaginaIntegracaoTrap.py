import time
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import ttk
from methods.str_para_funcao import *
from methods.integracao.trapezios import *

FONTE = ("Verdana", 12)
FONTE_TEXTO =  ("Verdana", 15)
FONTE_TITULO = ("Verdana", 15, "bold")

BUTTON_WIDTH = 40
BUTTON_FILL = "y"

BG_COLOR = "#1A5276"

class PaginaIntegracaoTrap(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self,
            text = "ITEGRAÇÃO TRAPÉZIOS",
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

        #------------------ pontos ------------------#
        pontos_container = tk.Label(self)
        pontos_container.pack(side = "top", pady = (20, 0))

        pontos_text = tk.Label(
            pontos_container,
            text = "Pontos [2, 1.000]:"
        ).pack(side = "left")

        self.pontos_entry = tk.Entry(
            pontos_container,
            width = BUTTON_WIDTH
        )
        self.pontos_entry.pack(side = "right")

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
            command = self.integrar_por_trapezios
        )
        calcular_button.pack(side = "top", fill = BUTTON_FILL, pady = 10)

        #----------------- resultado -----------------------#
        self.resultado_area = tk.Label(
            self,
            text = "Raiz:\n"
        ) 
        self.resultado_area.pack(side = "top", fill = BUTTON_FILL, pady = 10)
        
        self.resultado_time = tk.Label(
            self,
            text = "Tempo de execução:\n"
        ) 
        self.resultado_time.pack(side = "top", fill = BUTTON_FILL, pady = 10)


        margin_label = tk.Label(self, bg = BG_COLOR)
        margin_label.pack(side = "bottom", fill = "x", pady = (10, 0))
    
    def integrar_por_trapezios(self):
        
        f = self.func_entry.get()
        f = expressao_generica(f)
        
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        
        pontos = int(self.pontos_entry.get())
        if pontos < 2:
            pontos = 2
        if pontos > 1_000:
            pontos = 1_000

        inicio = time.time()
        area = regra_trapezios(f.f, a, b, pontos)
        fim = time.time()
        self.resultado_area["text"] = "Área:\n{}".format(area)

        self.resultado_time["text"] = "Tempo de execução:\n{}".format(fim - inicio)
        self.update_idletasks()

        # plot do grafico #
        if self.graph.get() == 1:
            grafico_trapezios(f.f, int(a), int(b), pontos, self.func_entry.get().replace("**", "^").replace("*", ""))
            plt.show()
