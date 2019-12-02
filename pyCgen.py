from tkinter import *
from tkinter.ttk import *
from struct_c import *
from struct_c import *

tipos = ['str','int','float','fk']
campos = []
lastRow = 2

def AgregarCampo():
    lastRow+1
    tipo_campo = Combobox(master=main,values=tipos).grid(row=lastRow)
    nombre_campo = Entry(master=main).grid(row=lastRow,column=1)
    campos.append = [tipo_campo,nombre_campo]
    return

main = Tk()
main.title("PyCGen")
Label(master=main,text='Estructura:').grid(row=0)
nombre_estrucutra = Entry(master=main)
nombre_estrucutra.grid(row=0,column=1)
Label(master=main,text='Campos:').grid(row=1)
Label(master=main,text='int').grid(row=2)
Label(master=main,text='id').grid(row=2,column=1)
btn_agregar_campo = Button(master=main,text='Agregar campo',command=AgregarCampo).grid(row=20)
main.mainloop()