import tkinter as tk
from tkinter import messagebox
import regex as re
from graphviz import Digraph

class Modelo:
    def __init__(self):
        pass

    def generar_automata(self, expresion_regular):
        try:
            automata = Digraph()
            automata.attr(rankdir='LR')

            # Convertir la expresión regular a un autómata
            regex = re.compile(expresion_regular)
            match = regex.match("abcdefghijklmnopqrstuvwxyz")  # Cadena más representativa
            if match is not None:
                automaton_description = match.to_dot()
                automata.body.append(automaton_description)

                return automata
            else:
                print("No se encontraron coincidencias para la expresión regular.")
                return None
        except Exception as e:
            print("Error:", e)

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Interprete de Expresiones Regulares")

        self.modelo = Modelo()

        self.expresion_label = tk.Label(root, text="Expresión regular:")
        self.expresion_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.expresion_entry = tk.Entry(root, width=30)
        self.expresion_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generar_button = tk.Button(root, text="Generar Autómata", command=self.generar_automata)
        self.generar_button.grid(row=0, column=2, padx=5, pady=5)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=1, columnspan=3, padx=5, pady=5)

    def generar_automata(self):
        expresion_regular = self.expresion_entry.get().strip()
        if not expresion_regular:
            messagebox.showwarning("Advertencia", "Por favor ingresa una expresión regular.")
            return

        automata = self.modelo.generar_automata(expresion_regular)
        if automata:
            automata.render('automata3', format='png', cleanup=True)
            img = tk.PhotoImage(file='automata3.png')
            self.canvas.create_image(0, 0, anchor='nw', image=img)
            self.canvas.image = img

def main():
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()

if __name__ == "__main__":
    main()
