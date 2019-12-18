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

class PaginaSobre(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self,
            text = "SOBRE",
            font = FONTE_TITULO,
            foreground = "white",
            bg = BG_COLOR,
            heigh = 4
        )
        title_label.pack(side = "top", fill = "x")
        
        texto_sobre_completo = "\n\nEsse é um app de código fonte livre para\nestudos e análise dos métodos numéricos por meio\n de um ambiente gráfico.\n\nVersão ALPHA 1.0\n\n\n\n\nFeito por:\nGustavo Cunha Lacerda\nEllian Aragão Dias\n\nPaper Clip Software"

        text_label = tk.Label(self, text=texto_sobre_completo, font=FONTE)
        text_label.pack(pady=10,padx=10)

        margin_label = tk.Label(self, bg = BG_COLOR)
        margin_label.pack(side = "bottom", fill = "x", pady = (10, 0))
