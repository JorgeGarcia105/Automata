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
        dot = Digraph(executable="C:/Program Files/Graphviz/bin/dot.exe")  # Ruta al ejecutable dot en tu sistema

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
        print("Se ha generado el archivo 'automata.png'.")

# Ejemplo de uso
if __name__ == "__main__":
    # Definición del autómata
    estados = {"q0", "q1", "q2"}
    alfabeto = {"a", "b"}
    transiciones = {
        ("q0", "a"): "q1",
        ("q1", "a"): "q1",
        ("q1", "b"): "q2",
        ("q2", "b"): "q2",
    }
    estado_inicial = "q0"
    estados_aceptacion = {"q2"}

    afd = AutomataDeterminista(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

    # Graficar el autómata
    afd.graficar()
