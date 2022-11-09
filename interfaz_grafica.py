from tkinter import *
from logica import *
from tkinter import messagebox


class Interfaz():

	root=Tk()

	logica=logic()
	base=call_database()

	resultados_label=Label()
	ingredientes_str=""
	resultados=""

	def __init__(self):

#-----------------------------Frames---------------------------


		spirits_frame=Frame(self.root)
		spirits_frame.grid(row=1, column=1, rowspan=4)
		#spirits_label=Label(spirits_frame, text="----Bebidas alcoholicas----").pack()
		#spirits_label.grid(row=0, column=0,padx=10, pady=10)

		#extras_frame=Frame(self.root)
		#extras_frame.grid(row=1, column=2, rowspan=4)
		#extras_label=Label(spirits_frame, text="----Extras----").pack()

		botones_frame=Frame(self.root)
		botones_frame.grid(row=5,column=1,columnspan=2)


		self.resultados_frame=Frame(self.root)
		self.resultados_frame.grid(row=1, column=3, rowspan=4)



		#-------------------------------bebidas-------------------

		Checkbutton(spirits_frame, text="Whisky escoces",anchor="w",width=30,
		command=lambda:self.ingredientes("whisky_escoces")).pack()
		Checkbutton(spirits_frame, text="Whisky Bourbon",anchor="w",width=30,
		command=lambda:self.ingredientes("whisky_bourbon")).pack()
		Checkbutton(spirits_frame, text="Vodka",anchor="w",width=30,
		command=lambda:self.ingredientes("vodka")).pack()
		Checkbutton(spirits_frame, text="Gin",anchor="w",width=30,
		command=lambda:self.ingredientes("gin")).pack()
		Checkbutton(spirits_frame, text="Tequila",anchor="w",width=30,
		command=lambda:self.ingredientes("tequila")).pack()
		Checkbutton(spirits_frame, text="Ron dorado",anchor="w",width=30,
		command=lambda:self.ingredientes("ron_dorado")).pack()
		Checkbutton(spirits_frame, text="Ron Blanco",anchor="w",width=30,
		command=lambda:self.ingredientes("ron_blanco")).pack()
		Checkbutton(spirits_frame, text="Fernet",anchor="w",width=30,
		command=lambda:self.ingredientes("fernet")).pack()
		Checkbutton(spirits_frame, text="Campari",anchor="w",width=30,
		command=lambda:self.ingredientes("campari")).pack()
		Checkbutton(spirits_frame, text="Aperol",anchor="w",width=30,
		command=lambda:self.ingredientes("aperol")).pack()
		Checkbutton(spirits_frame, text="Vermuth Rosso",anchor="w",width=30,
		command=lambda:self.ingredientes("vermuth_rosso")).pack()



		Checkbutton(spirits_frame, text="Almibar",anchor="w",width=30,
		command=lambda:self.ingredientes("almibar")).pack()
		Checkbutton(spirits_frame, text="Almibar de miel",anchor="w",width=30,
		command=lambda:self.ingredientes("almibar_miel")).pack()
		Checkbutton(spirits_frame, text="Jugo de limon",anchor="w",width=30,
		command=lambda:self.ingredientes("jugo_limon")).pack()
		Checkbutton(spirits_frame, text="Jengibre",anchor="w",width=30,
		command=lambda:self.ingredientes("jengibre")).pack()
		Checkbutton(spirits_frame, text="Menta",anchor="w",width=30,
		command=lambda:self.ingredientes("menta")).pack()
		Checkbutton(spirits_frame, text="Coca Cola",anchor="w",width=30,
		command=lambda:self.ingredientes("coca")).pack()
		Checkbutton(spirits_frame, text="Agua tonica",anchor="w",width=30,
		command=lambda:self.ingredientes("agua_tonica")).pack()
		Checkbutton(spirits_frame, text="Lima",anchor="w",width=30,
		command=lambda:self.ingredientes("lima")).pack()
		Checkbutton(spirits_frame, text="Soda",anchor="w",width=30,
		command=lambda:self.ingredientes("soda")).pack()


		#-------------Botones------------------

		self.agregar_string=StringVar()
		self.agregar_string.set("")
		self.agregar_texto=Entry(botones_frame, textvariable=self.agregar_string)
		self.agregar_texto.grid(row=0, column=2)

		agregar_button=Button(botones_frame, text="Agregar cocktail",command=lambda:self.add(self.agregar_texto.get(),self.logica.ingredientes_array))
		agregar_button.grid(row=1, column=2, padx=10)

		seeAll_button=Button(botones_frame, text="Ver todos", command=lambda:self.see())
		seeAll_button.grid(row=1, column=3, padx=10)

		quitar_button=Button(botones_frame, text="Quitar cocktail", command=lambda:self.remove_cocktail(self.agregar_texto.get()))
		quitar_button.grid(row=1, column=4, padx=10)



		#------------resultado----------------

		self.resultados_label=Label(self.resultados_frame)
		self.resultados_label.pack()







		self.root.mainloop()

	def ingredientes(self,ingrediente):

		self.logica.create_ingredientes_array(ingrediente)
		self.result()



	def result(self):


		self.resultados=self.logica.filtro(self.logica.ingredientes_array)
		self.resultados_label.config(text=self.resultados)



	def add(self,nombre,ingredientes):

		cocktail=[nombre,ingredientes]

		self.logica.add(cocktail)
		self.agregar_string.set("")

		if self.logica.error==1:

			messagebox.showinfo("Error", "Ya hay un cocktail con ese nombre")

		elif self.logica.error==0:

			messagebox.showinfo("","El cocktail se ha agregado con exito" )

		elif self.logica.error==2:

			messagebox.showinfo("Error", "El cocktail no puede no tener ingredientes")

		elif self.logica.error==3:

			messagebox.showinfo("Error", "El nombre del cocktail no puede quedar en blanco")


	def see(self):

		self.resultados=self.logica.seeAll()
		self.resultados_label.config(text=self.resultados)

	def remove_cocktail(self,cocktail):

		self.logica.remove(cocktail)

		if self.logica.error == 0:

			self.agregar_string.set("")
			messagebox.showinfo("","El cocktail ha sido removido con exito")

		else:

			messagebox.showinfo("Error","No existe un cocktail con ese nombre en la base de datos")



ventana=Interfaz()