import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

FONTE = ("Verdana", 12)
FONTE_TEXTO =  ("Verdana", 15)
FONTE_TITULO = ("Verdana", 15, "bold")

BUTTON_WIDTH = 40
BUTTON_FILL = "y"

BG_COLOR = "#1A5276"

class PaginaTutorial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self,
            text = "TUTORIAL",
            font = FONTE_TITULO,
            foreground = "white",
            bg = BG_COLOR,
            heigh = 4
        )
        title_label.pack(side = "top", fill = "x")
        texto_tutorial_completo = "Para utilizar o app basta selecionar o método\n desejado e informar o que é pedido\n\nFUNÇÕES: preferível usar os operadores de equações do python\n- suporte para funções trigonométricas em inglês (sin, cos)\n- suporte para multiplicação implícita 2x = 2*x\n- suporte para potências x**2 == x^2\n\nVETORES: quando pedidos separar\npor vírgula como o interior de um vetor declarado em python\n Ex.: 5, 6.5, 3, 4\n\nNÚMEROS REAIS: números reais dever ser informados com ponto\nEx.: 2.4, 12.555"
        text_label = tk.Label(self, text=texto_tutorial_completo, font=FONTE)
        text_label.pack(pady=10,padx=10)

        margin_label = tk.Label(self, bg = BG_COLOR)
        margin_label.pack(side = "bottom", fill = "x", pady = (10, 0))
