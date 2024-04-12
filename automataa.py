import tkinter as tk
from tkinter import messagebox
from graphviz import Digraph

class State:
    def __init__(self, label):
        self.label = label
        self.transitions = {}
        self.is_accepting = False  # Nuevo atributo para marcar el estado de aceptación

    def add_transition(self, symbol, state):
        if symbol in self.transitions:
            self.transitions[symbol].add(state)
        else:
            self.transitions[symbol] = {state}

class NFA:
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

class Modelo:
    def __init__(self):
        pass

    def regex_to_nfa(self, expresion_regular):
        stack = []
        states_count = 0

        def add_concatenation(s):
            nonlocal states_count
            states_count += 1
            new_state = State(states_count)
            s2 = stack.pop()
            s1 = stack.pop()
            s1.add_transition('', s2)  # Cambio aquí para la concatenación
            stack.append(s1)
            stack.append(new_state)

        for c in expresion_regular:
            if c == '.':
                add_concatenation('.')
            elif c == '|':
                # Implementacion de la lógica para el operador OR en la expresión regular
                states_count += 1
                new_state = State(states_count)
                s2 = stack.pop()
                s1 = stack.pop()
                new_state.add_transition('', s1)
                new_state.add_transition('', s2)
                states_count += 1
                accept_state = State(states_count)
                accept_state.is_accepting = True  # Marcar el estado de aceptación
                s1.add_transition('', accept_state)
                s2.add_transition('', accept_state)
                stack.append(new_state)
            elif c == '?':
                # Implementar la lógica para el operador de cero o una repetición
                s = stack.pop()
                s.is_accepting = True  # Marcar el estado de aceptación
                states_count += 1
                new_state = State(states_count)
                s.add_transition('', new_state)
                stack.append(s)
                stack.append(new_state)
            elif c == '+':
                # Implementar la lógica para el operador de una o más repeticiones
                s = stack.pop()
                s.is_accepting = True  # Marcar el estado de aceptación
                states_count += 1
                new_state = State(states_count)
                s.add_transition('', new_state)
                new_state.add_transition('', s)
                stack.append(s)
                stack.append(new_state)
            elif c == '*':
                # Implementar la lógica para el operador de cero o más repeticiones
                s = stack.pop()
                s.is_accepting = True  # Marcar el estado de aceptación
                states_count += 1
                new_state = State(states_count)
                s.add_transition('', new_state)
                new_state.add_transition('', s)
                stack.append(new_state)
            else:
                states_count += 1
                new_state = State(states_count)
                new_state.add_transition(c, None)
                stack.append(new_state)

        accept_state = State(states_count + 1)  # Nuevo estado de aceptación
        accept_state.is_accepting = True
        for state in stack:
            if state.is_accepting:
                state.add_transition('', accept_state)

        return NFA(stack[0], accept_state)

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

        nfa = self.modelo.regex_to_nfa(expresion_regular)
        automata = self.convert_nfa_to_digraph(nfa)
        if automata:
            automata.render('automata', format='png', cleanup=True)
            img = tk.PhotoImage(file='automata.png')
            self.canvas.create_image(0, 0, anchor='nw', image=img)
            self.canvas.image = img

    def convert_nfa_to_digraph(self, nfa):
        automata = Digraph()
        automata.attr(rankdir='LR')

        visited = set()

        def dfs(state):
            if state in visited:
                return
            visited.add(state)
            automata.node(str(state.label))
            if state.is_accepting:
                automata.attr('node', shape='doublecircle')

            for symbol, next_states in state.transitions.items():
                for next_state in next_states:
                    if symbol == '':
                        automata.edge(str(state.label), str(next_state.label), label='ε')
                    else:
                        automata.edge(str(state.label), str(next_state.label), label=symbol)
                    dfs(next_state)

        dfs(nfa.initial)
        return automata

def main():
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()

if __name__ == "__main__":
    main()
