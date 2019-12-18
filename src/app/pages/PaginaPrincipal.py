import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

from PaginaPrincipal import *
from PaginaSobre import *
from PaginaTutorial import *
from PaginaBissecao import *
from PaginaRaizNewton import *
from PaginaInterpNewton import *
from PaginaInterpMMQ import *
from PaginaIntegracaoTrap import *
from PaginaIntegracaoSimp import *

FONTE = ("Verdana", 12)
FONTE_TEXTO =  ("Verdana", 15)
FONTE_TITULO = ("Verdana", 15, "bold")

BUTTON_WIDTH = 40
BUTTON_FILL = "y"

BG_COLOR = "#1A5276"


class PaginaInicial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #---------- raizes de funcoes ------------------#
        title_label = tk.Label(
            self,
            text = "CÁLCULO NUMÉRICO",
            font = FONTE_TITULO,
            foreground = "white",
            bg = BG_COLOR,
            heigh = 4,
        )
        title_label.pack(side = "top", fill = "x")

        raiz_title = tk.Label(
            self,
            text = "Raízes de funções:",
            font = FONTE_TEXTO
        )
        raiz_title.pack(side = "top", fill = "x", pady = 10)

        bissecao_button = tk.Button(
            self,
            text = "Bisseção",
            bg = "white",
            width = BUTTON_WIDTH,
            command = lambda: controller.show_frame(PaginaBissecao)
        )
        bissecao_button.pack(fill = "y", expand=1)

        newton_button = tk.Button(
            self,
            text = "Newton",
            bg = "white",
            width = BUTTON_WIDTH,
            command = lambda: controller.show_frame(PaginaRaizNewton)
        )
        newton_button.pack(fill = BUTTON_FILL, expand=1)


        #------------ interpolação -----------------#
        interpolacao_title = tk.Label(
            self,
            text = "Interpolação de pontos:",
            font = FONTE_TEXTO
        )
        interpolacao_title.pack(side = "top", fill = "x", pady = 10)

        newton_interp_button = tk.Button(
            self,
            text = "Newton",
            bg = "white",
            width = BUTTON_WIDTH,
            command = lambda: controller.show_frame(PaginaInterpNewton)
        )
        newton_interp_button.pack(fill = BUTTON_FILL, expand=1)

        mmq_button = tk.Button(
            self,
            text = "Minimos Quadrados",
            bg = "white",
            width = BUTTON_WIDTH,
            command = lambda: controller.show_frame(PaginaInterpMMQ)
        )
        mmq_button.pack(fill = BUTTON_FILL, expand=1)

        #------------ integracao numerica ---------------#
        integracao_title = tk.Label(
            self,
            text = "Integração numérica:",
            font = FONTE_TEXTO
        )
        integracao_title.pack(side = "top", fill = "x", pady = 10)

        trapezios_button = tk.Button(
            self,
            text = "Trapézios",
            bg = "white",
            width = BUTTON_WIDTH,
            command = lambda: controller.show_frame(PaginaIntegracaoTrap)
        )
        trapezios_button.pack(fill = BUTTON_FILL, expand=1)

        simpson_button = tk.Button(
            self,
            text = "Simpson",
            bg = "white",
            width = BUTTON_WIDTH,
            command = lambda: controller.show_frame(PaginaIntegracaoSimp)
        )
        simpson_button.pack(fill = BUTTON_FILL, expand=1)
        
        margin_label = tk.Label(self, bg = BG_COLOR)
        margin_label.pack(side = "bottom", fill = "x", pady = (10, 0))