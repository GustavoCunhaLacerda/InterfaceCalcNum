import time
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import ttk
from methods.str_para_funcao import *
from methods.interp.newton import *

FONTE = ("Verdana", 12)
FONTE_TEXTO =  ("Verdana", 15)
FONTE_TITULO = ("Verdana", 15, "bold")

BUTTON_WIDTH = 40
BUTTON_FILL = "y"

BG_COLOR = "#1A5276"

class PaginaInterpNewton(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self,
            text = "INTERPOLAÇÃO NEWTON",
            font = FONTE_TITULO,
            foreground = "white",
            bg = BG_COLOR,
            heigh = 4
        )
        title_label.pack(side = "top", fill = "x")
        
        #-------------- x inicial ------------------#
        x_label = tk.Label(self)
        x_label.pack(side = "top", pady=(15, 5))

        x_text = tk.Label(x_label, text = "x1, x2, ..., xn : ").pack(side = "left")
        self.x_entry = tk.Entry(x_label, width = 30)
        self.x_entry.pack(side = "right")

        #-------------- y inicial ------------------#
        y_label = tk.Label(self)
        y_label.pack(side = "top")

        y_text = tk.Label(y_label, text = "y1, y2, ..., yn : ").pack(side = "left")
        self.y_entry = tk.Entry(y_label, width = 30)
        self.y_entry.pack(side = "right")

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
            command = self.calcular_interpolacao_newton
        )
        calcular_button.pack(side = "top", fill = BUTTON_FILL, pady = 10)

        #----------------- resultado -----------------------#
        self.resultado_poly = tk.Label(
            self,
            text = "Polinômio:\n"
        ) 
        self.resultado_poly.pack(side = "top", fill = BUTTON_FILL, pady = 10)
        
        self.resultado_time = tk.Label(
            self,
            text = "Tempo de execução:\n"
        ) 
        self.resultado_time.pack(side = "top", fill = BUTTON_FILL, pady = 10)

        ##

        margin_label = tk.Label(self, bg = BG_COLOR)
        margin_label.pack(side = "bottom", fill = "x", pady = (10, 0))

    def calcular_interpolacao_newton(self):

        x_vet = [float(x) for x in (self.x_entry.get()).split(',')]
        y_vet = [float(y) for y in (self.y_entry.get()).split(',')]

        inicio = time.time()
        poli = calc_interp_newton(x_vet, y_vet)
        fim = time.time()

        self.resultado_poly["text"] = "Polinômio:\nPn(x) = {}".format(poli.replace('**', '^').replace('*', ''))
        self.resultado_time["text"] = "Tempo de execução:\n{}".format(fim-inicio)

        self.update_idletasks()

        ## plot do grafico
        if self.graph.get() == 1:
            f = expressao_generica(poli.replace('^', '**'))

            grafico_calc_interp_newton(f.f, x_vet, y_vet, poli.replace('**', '^').replace('*', ''))
            plt.show()
