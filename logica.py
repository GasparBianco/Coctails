from bases import *

class Logica():


	error=0

	def __init__(self):

		self.base=Base_de_datos()

	def add_cocktail(self,cocktail):

		datos=self.base.seeAll()

		for registro in datos:

			if registro[1]==cocktail[0]:

				self.error=1

		if self.error==0:

			self.base.add_cocktail(cocktail)



	def remove_cocktail(self,cocktail):

		datos=self.base.seeAll()
		self.error=1

		for registro in datos:

			if registro[1]==cocktail[0]:

				self.error=0

		if self.error==0:

			self.base.remove_cocktail(cocktail)


	def seeAll(self):

		cocktails=self.base.seeAll()
		resultado=""

		for cocktail in cocktails:

			resultado=resultado +"\n" + cocktail[0]

		return resultado



	def filtro(self,ingredientes_disponibles):


		cocktails=self.base.seeAll()

		ingredientes_disponibles=ingredientes_disponibles.split()
		resultado=""



		for cocktail in cocktails:

			ingredientes_necesarios=cocktail[2].split()

			count_needed=0
			count=0


			for ingrediente in ingredientes_necesarios:

				count_needed=count_needed+1

				for ingredientes_disponible in ingredientes_disponibles:

					if ingredientes_disponible==ingrediente:

						count=count+1



			if count_needed==count:

				resultado=resultado +"\n" + cocktail[1]


		return resultado
