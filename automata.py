import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Modelo
class ExpresionRegular:
    def __init__(self, expresion):
        self.expresion = expresion

    def convertir_a_automata(self):
        estados = set()
        alfabeto = {'a', 'b'}
        transiciones = {}
        estado_inicial = None
        estados_aceptacion = set()

        estado_inicial = 0
        estados.add(estado_inicial)
        estados_aceptacion.add(estado_inicial)
        transiciones[(estado_inicial, 'ε')] = {1}
        transiciones[(1, 'ε')] = {estado_inicial}

        # Agregar transiciones ε adicionales si es necesario
        for estado in estados:
            if (estado, 'ε') not in transiciones:
                transiciones[(estado, 'ε')] = set()

        return Automata(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

class Automata:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion

    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = next(iter(self.transiciones[(estado_actual, simbolo)]))
            else:
                return False
        return estado_actual in self.estados_aceptacion

    def graficar(self, master):
        G = nx.DiGraph()

        for estado in self.estados:
            if estado in self.estados_aceptacion:
                G.add_node(estado, aceptacion=True)
            else:
                G.add_node(estado, aceptacion=False)

        for transicion, destinos in self.transiciones.items():
            origen, simbolo = transicion
            for destino in destinos:
                G.add_edge(origen, destino, simbolo=simbolo)

        fig, ax = plt.subplots()
        pos = nx.spring_layout(G)
        labels = {(origen, destino): simbolo for (origen, simbolo, destino) in G.edges(data='simbolo')}
        aceptacion = {estado: estado for estado, aceptacion in nx.get_node_attributes(G, 'aceptacion').items() if aceptacion}
        nx.draw(G, pos, with_labels=True, labels=labels, node_color='skyblue', node_size=1500, ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=aceptacion.keys(), node_color='salmon', node_size=1500, ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Controlador
class ControladorExpresionRegular:
    def __init__(self):
        self.expresion_regular = None

    def ingresar_expresion(self, expresion):
        self.expresion_regular = ExpresionRegular(expresion)

    def obtener_automata(self):
        if self.expresion_regular:
            return self.expresion_regular.convertir_a_automata()
        else:
            return None

    def guardar_expresion(self, expresion):
        print("Expresión regular guardada en la base de datos:", expresion)

# Vista (Interfaz de usuario)
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.controlador = ControladorExpresionRegular()

        # Interfaz de usuario
        self.frame_expresion = ttk.Frame(self.root)
        self.frame_expresion.pack(pady=10)

        self.label_expresion = ttk.Label(self.frame_expresion, text="Expresión regular:")
        self.label_expresion.grid(row=0, column=0, padx=5, pady=5)

        self.entry_expresion = ttk.Entry(self.frame_expresion, width=30)
        self.entry_expresion.grid(row=0, column=1, padx=5, pady=5)

        self.button_ingresar = ttk.Button(self.frame_expresion, text="Ingresar", command=self.ingresar_expresion)
        self.button_ingresar.grid(row=0, column=2, padx=5, pady=5)

        self.frame_cadena = ttk.Frame(self.root)
        self.frame_cadena.pack(pady=10)

        self.label_cadena = ttk.Label(self.frame_cadena, text="Cadena:")
        self.label_cadena.grid(row=0, column=0, padx=5, pady=5)

        self.entry_cadena = ttk.Entry(self.frame_cadena, width=30)
        self.entry_cadena.grid(row=0, column=1, padx=5, pady=5)

        self.button_validar = ttk.Button(self.frame_cadena, text="Validar", command=self.validar_cadena)
        self.button_validar.grid(row=0, column=2, padx=5, pady=5)

    def ingresar_expresion(self):
        expresion = self.entry_expresion.get()
        if expresion:
            self.controlador.ingresar_expresion(expresion)
            automata = self.controlador.obtener_automata()
            if automata:
                self.mostrar_automata(automata)
                automata.graficar(self.root)
            else:
                messagebox.showerror("Error", "La expresión regular no es válida.")
        else:
            messagebox.showerror("Error", "Debe ingresar una expresión regular.")

    def validar_cadena(self):
        cadena = self.entry_cadena.get()
        if cadena:
            automata = self.controlador.obtener_automata()
            if automata:
                if automata.validar_cadena(cadena):
                    messagebox.showinfo("Resultado", "La cadena es aceptada por el autómata.")
                else:
                    messagebox.showinfo("Resultado", "La cadena no es aceptada por el autómata.")
            else:
                messagebox.showerror("Error", "Debe ingresar una expresión regular primero.")
        else:
            messagebox.showerror("Error", "Debe ingresar una cadena.")

    def mostrar_automata(self, automata):
        if automata:
            print("Estados:", automata.estados)
            print("Alfabeto:", automata.alfabeto)
            print("Transiciones:")
            for transicion, destino in automata.transiciones.items():
                print(transicion, "->", destino)
            print("Estado inicial:", automata.estado_inicial)
            print("Estados de aceptación:", automata.estados_aceptacion)
        else:
            print("No se ha ingresado una expresión regular todavía.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplicación de Expresiones Regulares y Autómatas")
    app = Aplicacion(root)
    root.mainloop()
