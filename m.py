from graphviz import Digraph
import os

class AutomataDeterminista:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion

    def procesar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False  # El símbolo no está en el alfabeto
            estado_actual = self.transiciones.get((estado_actual, simbolo), None)
            if estado_actual is None:
                return False  # No hay transición para el símbolo actual
        return estado_actual in self.estados_aceptacion

    def graficar(self):
        dot = Digraph()  # No need for the 'executable' parameter here

        for estado in self.estados:
            if estado in self.estados_aceptacion:
                dot.node(estado, shape='doublecircle')
            else:
                dot.node(estado)

        dot.edge('', self.estado_inicial)

        for transicion, destino in self.transiciones.items():
            origen, simbolo = transicion
            dot.edge(origen, destino, label=simbolo)

        dot.render('automata', format='png', cleanup=True)
        print("Se ha generado el archivo 'automata5.png'.")

def leer_dfa(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        estados = set(file.readline().strip().split(','))
        alfabeto = set(file.readline().strip().split(','))
        estado_inicial = file.readline().strip()
        estados_aceptacion = set(file.readline().strip().split(','))

        transiciones = {}
        for line in file:
            origen, simbolo, destino = line.strip().split(',')
            transiciones[(origen, simbolo)] = destino

    return AutomataDeterminista(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

# Ejemplo de uso
if __name__ == "__main__":
    # Leer DFA desde un archivo
    dfa = leer_dfa("dfa.txt")

    # Graficar el autómata
    dfa.graficar()
