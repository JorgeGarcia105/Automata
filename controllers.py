import tkinter as tk
from models import Automata

class InterfazGrafica:
    def __init__(self, automata):
        self.automata = automata
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        self.dibujar_automata()
        self.root.mainloop()

    def dibujar_automata(self):
        # Dibujar estados
        for estado in self.automata.estados:
            x = 50 + estado * 100
            y = 150
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, outline="black", fill="white")
            self.canvas.create_text(x, y, text=str(estado), fill="black")

        # Dibujar transiciones
        for estado, transiciones in self.automata.transiciones.items():
            for simbolo, destinos in transiciones.items():
                for destino in destinos:
                    x1 = 50 + estado * 100
                    y1 = 150
                    x2 = 50 + destino * 100
                    y2 = 150
                    self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                    x_text = (x1 + x2) / 2
                    y_text = (y1 + y2) / 2
                    self.canvas.create_text(x_text, y_text, text=simbolo, fill="black")

# Ejemplo de uso
expresion_regular = "abc*"
automata = Automata.generar_automata(expresion_regular)
interfaz = InterfazGrafica(automata)
