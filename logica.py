import sqlite3

class Base_de_datos():

	
	error=0
	cocktails=sqlite3.connect("Cocteles")
	cursor=cocktails.cursor()


	def __init__(self):

		cocktails=sqlite3.connect("Cocteles")

		try:

			self.cursor.execute("""
				CREATE TABLE COCTELES (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				COCKTAIL VARCHAR(20),
				INGREDIENTES VARCHAR(100))
				""")

		except:
			sqlite3.OperationalError

	def add_cocktail(self,cocktail):
		
			
		self.cursor.execute("SELECT * FROM COCTELES")
		datos=self.cursor.fetchall()
			

		for registro in datos:

			if registro[1]==cocktail[0]:

				self.error=1
					
		if self.error==0:
				
			self.cursor.execute("INSERT INTO COCTELES VALUES (NULL,?,?)",cocktail)
			self.cocktails.commit()
				#self.cocktails.close()



	def remove_cocktail(self,cocktail):

		orden="DELETE FROM COCTELES WHERE COCKTAIL='"+cocktail+"'"
		print(orden)
		self.cursor.execute(orden)
		self.cocktails.commit()
		

	def seeAll(self):

		self.cursor.execute("SELECT COCKTAIL FROM COCTELES")
		cocktails=self.cursor.fetchall()
		resultado=""

		for cocktail in cocktails:
			
			resultado=resultado +"\n" + cocktail[0]

		return resultado

		

	def filtro(self,ingredientes_disponibles):
		
		self.cursor.execute("SELECT * FROM COCTELES")
		cocktails=self.cursor.fetchall()
		
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






