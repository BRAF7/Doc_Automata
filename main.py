from read_and_run import leer
from read_and_run import ejecutar
from tkinter import Label, Tk, Button, font,Entry, filedialog, messagebox

global_archivo = ''

def abrir_archivo():
    archivo = filedialog.askopenfilename(initialdir='./',title='Seleccionar un archivo',filetypes=(('text files','*.txt'),('all files',"*.*")))
    global global_archivo
    global_archivo = archivo

def ejecutar_automata():
    try:
        resultado['text'] = ''
        texto = texto_cadena.get()
        my_auto,auto_type = leer(global_archivo)
        my_resultado = ejecutar(my_auto,auto_type,texto)
        resultado['text'] = my_resultado
    except FileNotFoundError:
        messagebox.showerror(title='Archivo no seleccionado', message='Archivo no seleccionado')

if __name__ == '__main__':
    root = Tk()
    root.title('Lector de autómatas')
    root.geometry("450x100")

    subir_archivo = Button(root,text='Abrir archivo', width=16,height=1, command=abrir_archivo)
    btn_ejecutar = Button(root,text='Ejecutar el autómata', command=ejecutar_automata)

    texto_cadena = Entry(root, width=20)
    resultado = Label(root, text='')

    #Fuentes de los elementos
    fuente_botones = font.Font(size=10)
    subir_archivo['font'] = fuente_botones
    btn_ejecutar['font'] = fuente_botones
    resultado['font'] = font.Font(size=12)
   
    #Posición de los elementos
    subir_archivo.place(x=0,y=0)
    texto_cadena.place(x=0,y=40)
    btn_ejecutar.place(x=0,y=75)
    resultado.place(x=200,y=40)

    root.mainloop()

    
