from bases import *

class call_database():


	error=0

	def __init__(self):

		self.base=Base_de_datos()

	def add_cocktail(self,cocktail):

			self.base.add_cocktail(cocktail)



	def remove_cocktail(self,cocktail):

			orden="DELETE FROM COCTELES WHERE COCKTAIL='"+cocktail+"'"
			self.cursor.execute(orden)
			self.cocktails.commit()


	def seeAll(self):

		cocktails=self.base.seeAll()
		return cocktails



class logic():

	base=Base_de_datos()
	error=0

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

	def seeAll(self):

		cocktails=self.base.seeAll()
		resultado=""

		for cocktail in cocktails:

			resultado=resultado +"\n" + cocktail[0]

		return resultado



	def remove(self,cocktail):

		datos=self.base.seeAll()
		self.error=1

		for registro in datos:

			if registro[1]==cocktail:

				self.error=0

		if self.error==0:

			self.base.remove_cocktail(cocktail)

	def add(self,cocktail):

		datos=self.base.seeAll()

		for registro in datos:

			if registro[1]==cocktail:

				self.error=1

		if self.error==0:

			self.base.add_cocktail(cocktail)
