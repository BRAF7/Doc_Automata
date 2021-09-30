def step_automata(automata, posicion, key):
    posicion = posicion.replace('{',"")
    posicion = posicion.replace('}',"")
    try:
         assert(key in automata["S"])
    except AssertionError:
        print(f'El Símbolo {key} no se encuentra en el alfabeto')
    try:
        assert(posicion in automata["Q"])
    except AssertionError:
        print(f'El Estado {key} no se encuentra en el Autómata')
    try:
        return automata["D"][(posicion,key)]
    except KeyError:
        return False

def run_automata(letra, automata):
    initial_state = automata["q0"]
    if letra=="":
        return initial_state
    else:
        res_step = step_automata(automata, initial_state, letra[0])
        if res_step == False: return res_step
        return run_automata_h(automata, letra[1:], res_step)

def run_automata_h(automata, letra, posicion):
    if letra=="":
        return posicion
    else:
        current_step = step_automata(automata, posicion, letra[0])
        if current_step == False: return current_step
        return run_automata_h(automata, letra[1:], current_step)

def iniciar_dfa(word,DFA):
        res = run_automata(word, DFA)
        if res == False: return res
        return  res in DFA["F"]