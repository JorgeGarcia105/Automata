class InterfazUsuario:
    def solicitar_expresion_regular(self):
        # Método para solicitar al usuario una expresión regular
        expresion_regular = input("Ingrese la expresión regular: ")
        return expresion_regular

    def mostrar_automata(self, automata):
        # Método para mostrar el autómata generado
        print("Estados:", automata.estados)
        print("Estados finales:", automata.estados_finales)
        print("Transiciones:", automata.transiciones)

    def mostrar_error(self, mensaje):
        # Método para mostrar mensajes de error
        print("Error:", mensaje)
