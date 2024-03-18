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

    # Prueba con cadenas
    cadena1 = "ab"
    cadena2 = "aaaab"
    print(f"¿'{cadena1}' es aceptada? {afd.procesar_cadena(cadena1)}")
    print(f"¿'{cadena2}' es aceptada? {afd.procesar_cadena(cadena2)}")
