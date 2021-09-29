import ast
from dfa import run_automata
from nfa import nfa_sim

def leer(filename):
    modelado = {}
    with open(filename,mode='r',encoding='utf-8') as f:
        for line in f:
            k, v = line.strip().split('=')
            modelado[k.strip()] = v.strip()
    modelado['S']  = modelado['S'][1:-1].replace(',','')
    s = set(modelado['S'])

    modelado['Q'] = modelado['Q'].replace('{','')
    modelado['Q'] = modelado['Q'].replace('}','')
    state_list = list(modelado['Q'].split(','))
    q = set(state_list)


    delta = modelado['D']
    delta = delta.replace(' ','')
    delta = delta.replace('{(','(')
    delta = delta.replace(')}',')') 
    delta = delta.replace("(","('")
    delta = delta.replace(",","','") 
    delta = delta.replace(")','",",") 
    check_nfa = ',{'
    if check_nfa in modelado['D']:
        type_automata = 'NFA' 
        delta = delta.replace(",'{",",{") 
        delta = delta.replace("{","{'") 
        delta = delta.replace("}","'}") 
        delta = delta.replace("},","}),")     
    else:
        type_automata = 'DFA'
        delta = delta.replace(",(","),(") 
        delta = delta.replace(")","')") 
    delta_list =list(ast.literal_eval(delta))
    estados = {}
    for state in delta_list:
        estados[(state[0],state[1])] = state[2]

    modelado['F'] = modelado['F'].replace('{','')
    modelado['F'] = modelado['F'].replace('}','')
    estado_final = list(modelado['F'].split(','))

    final = set(estado_final)
    modelado = {
        'S': s,
        'Q': q,
        'D': estados,
        'q0':modelado['q0'],
        'F': final
    }
    return modelado,type_automata

def ejecutar(automata,tipo_automata):
    if tipo_automata == 'NFA':
        print('Ejecutando NFA')
        texto = input('Ingrese dato: ')
        res = nfa_sim(texto,automata['q0'],automata['D'],automata['F'],automata['S'])
    elif tipo_automata == 'DFA':
        print('Ejecutando DFA')
        texto = input('Ingrese dato: ')
        res = run_automata(texto,automata)
    if res:
        response = 'OK'
    else:
        response = 'NO OK'
    return response