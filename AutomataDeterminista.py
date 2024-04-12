from graphviz import Digraph
import re

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
        dot = Digraph()

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

def leer_dfa_desde_entrada():
    # Definir detalles del DFA
    estados = {'q0', 'q1', 'q2'}
    alfabeto = {'0', '1'}
    estado_inicial = 'q0'
    estados_aceptacion = {'q2'}

    # Definir las transiciones del DFA
    transiciones = {
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q0',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q0',
        ('q2', '0'): 'q2',
    }

    return AutomataDeterminista(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

def main():
    # Leer DFA desde la entrada del usuario
    dfa = leer_dfa_desde_entrada()

    # Graficar el autómata
    dfa.graficar()

if __name__ == "__main__":
    main()
