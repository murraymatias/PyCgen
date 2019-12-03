from tkinter import *
from tkinter.ttk import *
from struct_c import *
from struct_c import *

items = []
tipos_dato = ['int','float','str','fk']

def agregar_field():
    items.append([Combobox(frame_fields,values=tipos_dato),Entry(frame_fields)])

    for index,item in enumerate(items):
        item[0].grid(row=index,padx=5,pady=10)
        item[1].grid(row=index,column=1,padx=5,pady=10)

    Tk.update(main)

main = Tk()
main.geometry("400x500")
main.title("PyCGen")

frame_fields = Frame(main)
frame_buttons = Frame(main)

btn_agregar = Button(frame_buttons,text='Agregar',command=agregar_field)
btn_salir = Button(frame_buttons,text='Salir',command=main.destroy)

btn_agregar.pack()
btn_salir.pack()

frame_fields.pack()
frame_buttons.pack(side=BOTTOM)

main.mainloop()