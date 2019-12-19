from tkinter import *
from tkinter.ttk import *
from entities import *
from fileIO import *

items = []
tipos_dato = ['INT','FLOAT','STR','FKEY']

def tipo_a_int(tipo):
    if(tipo == 'INT'):
        return 0
    elif(tipo == 'FLOAT'):
        return 1
    elif(tipo == 'STR'):
        return 2
    elif(tipo == 'FKEY'):
        return 3
    else:
        raise Exception("Tipo de campo invalido")

def agregar_field():
    if(len(items) < 6):
        items.append([Combobox(frame_fields,values=tipos_dato),Entry(frame_fields)])

        for index,item in enumerate(items):
            item[0].grid(row=index+3,padx=5,pady=5)
            item[1].grid(row=index+3,column=1,padx=5,pady=5)

        Tk.update(main)

def quitar_field():
    if(len(items) > 0):
        item = items.pop()

        item[0].grid_forget()
        item[1].grid_forget()

        Tk.update(main)

def crear_estructura():
    campos = []
    for item in items:
        campos.append(Campo(tipo_a_int(item[0].get()),item[1].get()))
    
    estructura = Estructura(txtb_nombre_estrectura.get(),campos)

    FileIO.SaveText(estructura.nombre_may + '.c',estructura.generar_cuerpo())
    FileIO.SaveText(estructura.nombre_may + '.h',estructura.generar_cuerpo_h())
    FileIO.SaveText('Parser.c',estructura.generar_parser_c())
    FileIO.SaveText('Parser.h',estructura.generar_parser_h())


main = Tk()
#main.geometry("400x500")
main.title("PyCGen")

frame_fields = Frame(main)
frame_buttons = Frame(main)

lbl_estructura = Label(frame_fields,text='Nombre estructura')
lbl_campos = Label(frame_fields,text='Campos (id ya incluido)')
lbl_id_int = Label(frame_fields,text='int')
lbl_id_nombre = Label(frame_fields,text="id")
txtb_nombre_estrectura = Entry(frame_fields)
lbl_estructura.grid(row=0,padx=5,pady=20)
txtb_nombre_estrectura.grid(row=0,column=1,padx=5,pady=20)
lbl_campos.grid(row=1,columnspan=2)
lbl_id_int.grid(row=2,padx=5,pady=10)
lbl_id_nombre.grid(row=2,column=1,padx=5,pady=10)

btn_agregar = Button(frame_buttons,text='Agregar campo',command=agregar_field)
btn_quitar = Button(frame_buttons,text='Quitar campo',command=quitar_field)
btn_salir = Button(frame_buttons,text='Salir',command=main.destroy)
btn_aceptar = Button(frame_buttons,text='Aceptar y crear',command=crear_estructura)

btn_agregar.config(width=30)
btn_quitar.config(width=30)
btn_salir.config(width=30)
btn_aceptar.config(width=30)

btn_agregar.grid(row=0, column=0,padx=2,pady=2)
btn_quitar.grid(row=0, column=1,padx=2,pady=2)
btn_salir.grid(row=1, column=0,padx=2,pady=2)
btn_aceptar.grid(row=1, column=1,padx=2,pady=2)

frame_fields.pack()
frame_buttons.pack(side=BOTTOM)

agregar_field()
main.mainloop()