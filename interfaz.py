from tkinter import *
from logica import *
from tkinter import messagebox


class Interfaz():

	root=Tk()


	ingredientes_str=""
	resultados=""

	whisky_escoces=BooleanVar()
	whisky_bourbon=BooleanVar()
	vodka=BooleanVar()
	gin=BooleanVar()
	tequila=BooleanVar()
	ron_dorado=BooleanVar()
	ron_blanco=BooleanVar()
	fernet=BooleanVar()
	campari=BooleanVar()
	aperol=BooleanVar()
	vermuth_rosso=BooleanVar()
	almibar=BooleanVar()
	almibar_miel=BooleanVar()
	jugo_limon=BooleanVar()
	jengibre=BooleanVar()
	menta=BooleanVar()
	coca=BooleanVar()
	soda=BooleanVar()
	agua_tonica=BooleanVar()
	lima=BooleanVar()

	def __init__(self):

#-----------------------------Frames---------------------------


		spirits_frame=Frame(self.root)
		spirits_frame.grid(row=1, column=1, rowspan=4)
		spirits_label=Label(spirits_frame, text="----Bebidas alcoholicas----").pack()
		#spirits_label.grid(row=0, column=0,padx=10, pady=10)

		extras_frame=Frame(self.root)
		extras_frame.grid(row=1, column=2, rowspan=4)
		extras_label=Label(extras_frame, text="----Extras----").pack()

		botones_frame=Frame(self.root)
		botones_frame.grid(row=5,column=1,columnspan=2)


		self.resultados_frame=Frame(self.root)
		self.resultados_frame.grid(row=1, column=3, rowspan=4)



		#-------------------------------bebidas-------------------

		Checkbutton(spirits_frame, text="Whisky escoces",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.whisky_escoces, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Whisky Bourbon",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.whisky_bourbon, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Vodka",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.vodka, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Gin",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.gin, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Tequila",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.tequila, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Ron dorado",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.ron_dorado, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Ron Blanco",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.ron_blanco, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Fernet",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.fernet, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Campari",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.campari, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Aperol",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.aperol, command=self.ingredientes).pack()
		Checkbutton(spirits_frame, text="Vermuth Rosso",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.vermuth_rosso, command=self.ingredientes).pack()



		Checkbutton(extras_frame, text="Almibar",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.almibar, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Almibar de miel",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.almibar_miel, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Jugo de limon",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.jugo_limon, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Jengibre",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.jengibre, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Menta",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.menta, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Coca Cola",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.coca, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Agua tonica",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.agua_tonica, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Lima",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.lima, command=self.ingredientes).pack()
		Checkbutton(extras_frame, text="Soda",anchor="w",width=30, onvalue=True, offvalue=False, variable=self.soda, command=self.ingredientes).pack()


		#-------------Botones------------------

		self.agregar_string=StringVar()
		self.agregar_string.set("")
		self.agregar_texto=Entry(botones_frame, textvariable=self.agregar_string)
		self.agregar_texto.grid(row=0, column=2)

		agregar_button=Button(botones_frame, text="Agregar cocktail",command=lambda:self.add(self.agregar_texto.get(),self.ingredientes_str))
		agregar_button.grid(row=1, column=2, padx=10)

		seeAll_button=Button(botones_frame, text="Ver todos", command=lambda:self.see())
		seeAll_button.grid(row=1, column=3, padx=10)

		quitar_button=Button(botones_frame, text="Quitar cocktail", command=lambda:self.remove_cocktail(self.agregar_texto.get()))
		quitar_button.grid(row=1, column=4, padx=10)



		#------------resultado----------------

		self.resultados_label=Label(self.resultados_frame)
		self.resultados_label.pack()







		self.root.mainloop()

	def ingredientes(self):

		self.ingredientes_str=""


		if self.whisky_escoces.get():

			self.ingredientes_str=self.ingredientes_str+"whisky_escoces "

		if self.whisky_bourbon.get():

			self.ingredientes_str=self.ingredientes_str+"whisky_bourbon "

		if self.vodka.get():

			self.ingredientes_str=self.ingredientes_str+"vodka "

		if self.gin.get():

			self.ingredientes_str=self.ingredientes_str+"gin "

		if self.tequila.get():

			self.ingredientes_str=self.ingredientes_str+"tequila "

		if self.ron_dorado.get():

			self.ingredientes_str=self.ingredientes_str+"ron_dorado "

		if self.ron_blanco.get():

			self.ingredientes_str=self.ingredientes_str+"ron_blanco "

		if self.fernet.get():

			self.ingredientes_str=self.ingredientes_str+"fernet "

		if self.campari.get():

			self.ingredientes_str=self.ingredientes_str+"campari "

		if self.aperol.get():

			self.ingredientes_str=self.ingredientes_str+"aperol "

		if self.vermuth_rosso.get():

			self.ingredientes_str=self.ingredientes_str+"vermuth_rosso "

		if self.almibar.get():

			self.ingredientes_str=self.ingredientes_str+"almibar "

		if self.almibar_miel.get():

			self.ingredientes_str=self.ingredientes_str+"almibar_miel "

		if self.jugo_limon.get():

			self.ingredientes_str=self.ingredientes_str+"jugo_limon "

		if self.jengibre.get():

			self.ingredientes_str=self.ingredientes_str+"jengibre "

		if self.menta.get():

			self.ingredientes_str=self.ingredientes_str+"menta "

		if self.coca.get():

			self.ingredientes_str=self.ingredientes_str+"coca "

		if self.soda.get():

			self.ingredientes_str=self.ingredientes_str+"soda "

		if self.lima.get():

			self.ingredientes_str=self.ingredientes_str+"lima "

		if self.agua_tonica.get():

			self.ingredientes_str=self.ingredientes_str+"agua_tonica "



		self.result()



	def result(self):

		self.resultados=logica.filtro(self.ingredientes_str)
		self.resultados_label.config(text=self.resultados)



	def add(self,nombre,ingredientes):

		cocktail=[nombre,ingredientes]

		logica.add_cocktail(cocktail)
		self.agregar_string.set("")
		#agregar_texto.config(textvariable=agregar_string)

		if logica.error==1:

			messagebox.showinfo("Error", "Ya hay un cocktail con ese nombre")



	def see(self):

		self.resultados=logica.seeAll()
		self.resultados_label.config(text=self.resultados)

	def remove_cocktail(self,cocktail):

		base.remove_cocktail(cocktail)

		if logica.error == 0:

			self.agregar_string.set("")

		else:

			messagebox.showinfo("Error","No existe un cocktail con ese nombre en la base de datos")



logica=Logica()
ventana=Interfaz()
