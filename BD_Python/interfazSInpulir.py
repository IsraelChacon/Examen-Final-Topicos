from tkinter import *
from tkinter import ttk
import ConexionYconsultas 

mysql = ConexionYconsultas.BD()
ventana = Tk()
ventana.title('Mysql con tkinter')
ventana.geometry('800x500')

nombre = StringVar()
correo = StringVar()
telefono = StringVar()
otro = StringVar()

marco = LabelFrame(ventana, text='Tabla entradasalidadinero')
marco.place(x=50,y=50,width=700,height=400)

lblNombre = Label(marco, text='Nombre: ').grid(column=0, row=0,padx=5,pady=5)
txtNombre = Entry(marco, textvariable=nombre).grid(column=1,row=0)

lblCorreo = Label(marco, text='Duracion: ').grid(column=2, row=0,padx=5,pady=5)
txtCorreo = Entry(marco, textvariable=correo).grid(column=3,row=0)

lblTelefono = Label(marco, text='Director: ').grid(column=0, row=1,padx=5,pady=5)
txtTelefono = Entry(marco, textvariable=telefono).grid(column=1,row=1)

lblTelefono = Label(marco, text='Genero: ').grid(column=2, row=1,padx=5,pady=5)
txtTelefono = Entry(marco, textvariable=otro).grid(column=3,row=1)

tvPersonas = ttk.Treeview(marco)
tvPersonas.grid(column=0,row=3,columnspan=4)
tvPersonas['columns'] = ('Id', 'Fecha', 'Tipo ing', 'Monto' ,'Nombre', 'Observaciones')
tvPersonas.column('#0', width=0, stretch=NO)
tvPersonas.column('Id', width=80, anchor=CENTER)
tvPersonas.column('Fecha', width=100, anchor=CENTER)
tvPersonas.column('Tipo ing', width=100, anchor=CENTER)
tvPersonas.column('Monto', width=100, anchor=CENTER)
tvPersonas.column('Nombre', width=100, anchor=CENTER)
tvPersonas.column('Observaciones', width=150, anchor=CENTER)
tvPersonas.heading('Id', text='Id', anchor=CENTER)
tvPersonas.heading('Fecha', text='Fecha', anchor=CENTER)
tvPersonas.heading('Tipo ing', text='Tipo ing', anchor=CENTER)
tvPersonas.heading('Monto', text='Monto', anchor=CENTER)
tvPersonas.heading('Nombre', text='Nombre', anchor=CENTER)
tvPersonas.heading('Observaciones', text='Observaciones', anchor=CENTER)

btnAgregar = Button(marco, text='Agregar', command=lambda:agregar()).grid(column=0,row=4,pady=4)

btnActualizar = Button(marco, text='Actualizar', command=lambda:actualizar()).grid(column=1,row=4,pady=4)

btnEliminar = Button(marco, text='Eliminar', command=lambda:Eliminar()).grid(column=2,row=4,pady=4)

def validar():
    return len(nombre.get()) and len(correo.get()) and len(telefono.get())

def limpiar():
    nombre.set('')
    correo.set('')
    telefono.set('')

def vaciar_tabla():
    filas = tvPersonas.get_children()
    for fila in filas:
        tvPersonas.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    consulta = mysql.select()
    for fila in consulta:
        id = fila[0]
        tvPersonas.insert('',END,text=id,values=fila)

def agregar():
    if validar():
        variables = nombre.get(), correo.get(), telefono.get(), otro.get()
        sql = "insert into pelicula(nombre_pelicula, duracion, id_genero, id_director) values('{}', '{}', '{}', '{}')".format(variables[0],variables[1],variables[2],variables[3])
        mysql.agregar(sql)
        llenar_tabla()
        limpiar()

def actualizar():
    variables = nombre.get(), correo.get(), telefono.get(), otro.get()
    sql = "update pelicula SET nombre_pelicula = '{}', duracion = '{}', id_genero = '{}', id_director = '{}' where nombre_pelicula= '"+str(id).format(variables[0],variables[1],variables[2],variables[3])
    mysql.agregar(sql)
    llenar_tabla()
    limpiar()

def Eliminar():
    item_seleccionado = tvPersonas.focus()
    detalle = tvPersonas.item(item_seleccionado)
    id = detalle.get('values')[0]
    if id > 0:
        sql = 'delete from pelicula where id = '+str(id)
        mysql.eliminar(sql)
        llenar_tabla()
    print(id)

llenar_tabla()
ventana.mainloop()
