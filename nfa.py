def nfa_sim(dato, actual, edges, accepting,sigma):
    if dato == "":
        return actual in accepting
    else:
        letter = dato[0]
        if letter not in sigma:
            return False
        key = (actual, letter)
        epsilon = False
        if key not in edges:
            key = (actual, 'epsilon')
            epsilon = True
        if key in edges:
            if epsilon:
                rest = dato
            else:
                rest = dato[1:]
            states = edges[key]
            for state in states:
                if nfa_sim(rest, state, edges, accepting,sigma):
                    return True
        return False
