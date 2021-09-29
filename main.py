from read_and_run import leer
from read_and_run import ejecutar




if __name__ == '__main__':
    new_NFA,auto_type = leer('test_dfa.txt')
    print(ejecutar(new_NFA,auto_type))
