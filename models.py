class Automata:
    def __init__(self):
        self.estados = []  # Lista de estados
        self.estados_finales = []  # Lista de estados finales
        self.transiciones = {}  # Diccionario de transiciones

    @classmethod
    def generar_automata(cls, expresion_regular):
        automata = cls()
        pila = []
        for simbolo in expresion_regular:
            if simbolo.isalpha():
                # Crear un nuevo estado y transición con el símbolo
                nuevo_estado = len(automata.estados)
                automata.estados.append(nuevo_estado)
                transicion = {simbolo: [nuevo_estado]}
                automata.transiciones[nuevo_estado] = transicion
                pila.append([nuevo_estado, nuevo_estado])
            elif simbolo == '*':
                # Realizar operación de clausura estrella sobre el último estado agregado
                estado = pila.pop()
                nuevo_estado = len(automata.estados)
                automata.estados.append(nuevo_estado)
                transicion = {'ε': [estado[0], nuevo_estado]}
                if estado[0] not in automata.transiciones:
                    automata.transiciones[estado[0]] = {}
                if 'ε' not in automata.transiciones[estado[0]]:
                    automata.transiciones[estado[0]]['ε'] = []
                automata.transiciones[estado[0]]['ε'].append(nuevo_estado)
                automata.transiciones[nuevo_estado] = {'ε': []}
                pila.append([nuevo_estado, nuevo_estado])
            elif simbolo == '+':
                # Realizar operación de concatenación sobre los últimos dos estados agregados
                estado2 = pila.pop()
                estado1 = pila.pop()
                transicion = {'ε': [estado1[1], estado2[0]]}
                if estado1[1] not in automata.transiciones:
                    automata.transiciones[estado1[1]] = {}
                if 'ε' not in automata.transiciones[estado1[1]]:
                    automata.transiciones[estado1[1]]['ε'] = []
                automata.transiciones[estado1[1]]['ε'].append(estado2[0])
                pila.append([estado1[0], estado2[1]])
            elif simbolo == '|':
                # Realizar operación de unión sobre los últimos dos estados agregados
                estado2 = pila.pop()
                estado1 = pila.pop()
                nuevo_estado = len(automata.estados)
                automata.estados.append(nuevo_estado)
                transicion = {'ε': [nuevo_estado, estado1[0]]}
                automata.transiciones[nuevo_estado] = {'ε': []}
                if estado1[0] not in automata.transiciones:
                    automata.transiciones[estado1[0]] = {}
                if 'ε' not in automata.transiciones[estado1[0]]:
                    automata.transiciones[estado1[0]]['ε'] = []
                automata.transiciones[estado1[0]]['ε'].append(nuevo_estado)
                transicion = {'ε': [nuevo_estado, estado2[0]]}
                if estado2[0] not in automata.transiciones:
                    automata.transiciones[estado2[0]] = {}
                if 'ε' not in automata.transiciones[estado2[0]]:
                    automata.transiciones[estado2[0]]['ε'] = []
                automata.transiciones[estado2[0]]['ε'].append(nuevo_estado)
                nuevo_estado2 = len(automata.estados)
                automata.estados.append(nuevo_estado2)
                transicion = {'ε': [estado1[1], nuevo_estado2]}
                if estado1[1] not in automata.transiciones:
                    automata.transiciones[estado1[1]] = {}
                if 'ε' not in automata.transiciones[estado1[1]]:
                    automata.transiciones[estado1[1]]['ε'] = []
                automata.transiciones[estado1[1]]['ε'].append(nuevo_estado2)
                transicion = {'ε': [estado2[1], nuevo_estado2]}
                if estado2[1] not in automata.transiciones:
                    automata.transiciones[estado2[1]] = {}
                if 'ε' not in automata.transiciones[estado2[1]]:
                    automata.transiciones[estado2[1]]['ε'] = []
                automata.transiciones[estado2[1]]['ε'].append(nuevo_estado2)
                pila.append([nuevo_estado, nuevo_estado2])
        # El autómata se construyó, ahora necesitas establecer los estados finales
        estado_final = pila.pop()
        automata.estados_finales = estado_final
        return automata
