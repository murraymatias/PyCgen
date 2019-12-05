from tkinter import *
from tkinter.ttk import *
from entities import *
from fileIO import *

items = []
tipos_dato = ['int','float','str','fk']

def tipo_a_int(tipo):
    if(tipo == 'int'):
        return 0
    elif(tipo == 'float'):
        return 1
    elif(tipo == 'str'):
        return 2
    elif(tipo == 'fk'):
        return 3
    else:
        raise Exception("Tipo de campo invalido")

def agregar_field():
    if(len(items) < 6):
        items.append([Combobox(frame_fields,values=tipos_dato),Entry(frame_fields)])

        for index,item in enumerate(items):
            item[0].grid(row=index+3,padx=5,pady=10)
            item[1].grid(row=index+3,column=1,padx=5,pady=10)

        Tk.update(main)

def crear_estructura():
    campos = []
    for item in items:
        campos.append(Campo(tipo_a_int(item[0].get()),item[1].get()))
    
    estructura = Estructura(txtb_nombre_estrectura.get(),campos)

    FileIO.SaveText('output\\',estructura.nombre_min + '.c',estructura.generar_cuerpo())
    FileIO.SaveText('output\\',estructura.nombre_min + '.h',estructura.generar_cuerpo_h())


main = Tk()
main.geometry("400x500")
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
btn_salir = Button(frame_buttons,text='Salir',command=main.destroy)
btn_aceptar = Button(frame_buttons,text='Aceptar y crear',command=crear_estructura)

btn_agregar.pack()
btn_salir.pack()
btn_aceptar.pack()

frame_fields.pack()
frame_buttons.pack(side=BOTTOM)

main.mainloop()