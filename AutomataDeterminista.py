from graphviz import Digraph

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

        dot.render('automata2', format='png', cleanup=True)
        print("Se ha generado el archivo 'automata2.png'.")

def leer_dfa_desde_entrada():
    print("Ingrese los detalles del DFA:")
    estados = set(input("Estados (separados por comas): ").strip().split(','))
    alfabeto = set(input("Alfabeto (separado por comas): ").strip().split(','))
    estado_inicial = input("Estado inicial: ").strip()
    estados_aceptacion = set(input("Estados de aceptación (separados por comas): ").strip().split(','))

    transiciones = {}
    while True:
        transicion = input("Ingrese una transición como 'estado_actual,símbolo,estado_siguiente' (o 'fin' para terminar): ").strip()
        if transicion.lower() == 'fin':
            break  # Sale del bucle mientras
        origen, simbolo, destino = transicion.split(',')
        transiciones[(origen, simbolo)] = destino

    return AutomataDeterminista(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)


# Ejemplo de uso
if __name__ == "__main__":
    # Leer DFA desde la entrada del usuario
    dfa = leer_dfa_desde_entrada()

    # Graficar el autómata
    dfa.graficar()
