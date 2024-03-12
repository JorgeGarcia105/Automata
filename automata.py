# Importamos las bibliotecas necesarias para graficar
import networkx as nx
import matplotlib.pyplot as plt

# Modelo
class ExpresionRegular:
    def __init__(self, expresion):
        self.expresion = expresion

    def convertir_a_automata(self):
        # Implementación básica de la conversión de expresiones regulares a DFA
        # Aquí se puede usar el algoritmo de construcción de subconjuntos
        # Para simplificar, este ejemplo solo manejará expresiones regulares con el alfabeto {a, b}
        estados = set()
        alfabeto = {'a', 'b'}
        transiciones = {}
        estado_inicial = None
        estados_aceptacion = set()

        # Algoritmo de construcción de subconjuntos
        # Simplemente se construye un autómata que acepta cualquier cadena con la expresión regular dada
        estado_inicial = 0
        estados.add(estado_inicial)
        estados_aceptacion.add(estado_inicial)
        transiciones[(estado_inicial, 'ε')] = {1}
        transiciones[(1, 'ε')] = {estado_inicial}

        return Automata(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)

class Automata:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion

    def validar_cadena(self, cadena):
        # Implementación de la validación de cadena utilizando el autómata
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if (estado_actual, simbolo) in self.transiciones:
                estado_actual = next(iter(self.transiciones[(estado_actual, simbolo)]))
            else:
                return False
        return estado_actual in self.estados_aceptacion

    def graficar(self):
        # Creamos un grafo dirigido utilizando NetworkX
        G = nx.DiGraph()

        # Agregamos los nodos al grafo
        for estado in self.estados:
            if estado in self.estados_aceptacion:
                G.add_node(estado, aceptacion=True)
            else:
                G.add_node(estado, aceptacion=False)

        # Agregamos las transiciones al grafo
        for transicion, destinos in self.transiciones.items():
            origen, simbolo = transicion
            for destino in destinos:
                G.add_edge(origen, destino, simbolo=simbolo)

        # Dibujamos el grafo
        pos = nx.spring_layout(G)  # Posiciones de los nodos
        labels = {(i, j): simbolo for i, j, simbolo in G.edges(data='simbolo')}  # Etiquetas de las transiciones
        aceptacion = {estado: estado for estado, aceptacion in nx.get_node_attributes(G, 'aceptacion').items() if aceptacion}  # Estados de aceptación
        nx.draw(G, pos, with_labels=True, labels=labels, node_color='skyblue', node_size=1500)
        nx.draw_networkx_nodes(G, pos, nodelist=aceptacion.keys(), node_color='salmon', node_size=1500)
        plt.show()

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
        # Aquí iría la lógica para guardar la expresión regular en una base de datos
        print("Expresión regular guardada en la base de datos:", expresion)

# Vista (Interfaz de usuario)
def mostrar_automata(automata):
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

# Ejemplo de uso
if __name__ == "__main__":
    controlador = ControladorExpresionRegular()
    expresion = input("Ingrese la expresión regular: ")
    controlador.ingresar_expresion(expresion)
    automata = controlador.obtener_automata()
    mostrar_automata(automata)

    cadena = input("Ingrese una cadena para validar: ")
    if automata:
        if automata.validar_cadena(cadena):
            print("La cadena es aceptada por el autómata.")
        else:
            print("La cadena no es aceptada por el autómata.")
    
    # Graficamos el autómata
    if automata:
        automata.graficar()
