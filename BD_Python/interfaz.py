from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width
import base_datos
# * = todo


#ventana principal
mysql = base_datos.BD()
ventana = Tk()
ventana.title("Películas")
ventana.geometry("1025x350")



#   Variables con tkinter de la tabla personas

pelicula = StringVar()
genero = StringVar()
duracion = StringVar()
nom_direc = StringVar()
#   Agregamos un LabelFrame
marco0 = LabelFrame(ventana, text = "")
marco0.place(x = 10, y = 10, width = 85, height = 300)

marco1 = LabelFrame(ventana, text = "")
marco1.place(x = 95, y = 10, width = 155, height = 300)

#marco para la tabla
marco2 = LabelFrame(ventana, text = "Tabla Peliculas")
marco2.place(x = 250, y = 10, width = 765, height = 300)

#   Agregamos Label y texinput para nombre, correo y telefono
lblPelicula = Label(marco1, text = "Película: ")
lblPelicula.grid(column = 0, row = 0, padx = 5, pady = 5)
txtPelicula = Entry(marco1, textvariable = pelicula)
txtPelicula.grid(column = 0, row = 1)

lblGenero = Label(marco1, text = "Género: ")
lblGenero.grid(column = 0, row = 2, padx = 5, pady = 5)
cmbgenero = ttk.Combobox(marco1, textvariable = genero)
cmbgenero.grid(column = 0, row = 3)

lblDuracion = Label(marco1, text = "Duración: ")
lblDuracion.grid(column = 0, row = 4, padx = 5, pady = 5)
txtDuracion = Entry(marco1, textvariable = duracion)
txtDuracion.grid(column = 0, row = 5)

lblDuracion = Label(marco1, text = "Director: ")
lblDuracion.grid(column = 0, row = 6, padx = 5, pady = 5)
txtDuracion = Entry(marco1, textvariable = duracion)
txtDuracion.grid(column = 0, row = 7)

#mensaje = Label(marco, text = "Contenido de la tabla", fg = "blue")
#mensaje.grid(column = 0, row = 2, columnspan = 4)

btnNuevo = Button(marco0, text = "Nuevo", command = lambda:agregar())
btnNuevo.grid(column = 4, row = 4, pady = 5,padx=10)

btnModificar = Button(marco0, text = "Modificar", command = lambda:actualizar())
btnModificar.grid(column = 4, row = 5, pady = 5, padx=10 )

btnEliminar = Button(marco0, text = "Eliminar", command = lambda:eliminar())
btnEliminar.grid(column = 4, row = 6, pady = 5,padx=10)

btnGuardar = Button(marco1, text = "Guardar", command = lambda:eliminar())
btnGuardar.grid(column = 0, row = 8, pady = 5,padx=10)

btnCancelar = Button(marco1, text = "Cancelar", command = lambda:eliminar())
btnCancelar.grid(column = 0, row = 9, pady = 5,padx=10)




#tabla de 5 columnas
tvPeliculas = ttk.Treeview(marco2)
tvPeliculas.grid(column = 0, row = 3, columnspan = 5, padx = 5)
tvPeliculas["columns"] = ("Id", "Pelicula", "Genero", "Duracion", "Director")
tvPeliculas.column("#0", width = 0, stretch = NO)
tvPeliculas.column("Id", width = 150, anchor = CENTER)
tvPeliculas.column("Pelicula", width = 150, anchor = CENTER)
tvPeliculas.column("Genero", width = 150, anchor = CENTER)
tvPeliculas.column("Duracion", width = 150, anchor = CENTER)
tvPeliculas.column("Director", width = 150, anchor = CENTER)
tvPeliculas.heading("Id", text = "Id", anchor = CENTER)
tvPeliculas.heading("Pelicula", text = "Película", anchor = CENTER)
tvPeliculas.heading("Genero", text = "Género", anchor = CENTER)
tvPeliculas.heading("Duracion", text = "Duración", anchor = CENTER)
tvPeliculas.heading("Director", text = "Director", anchor = CENTER)


#inicializar
ventana.mainloop()