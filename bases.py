import sqlite3

class Base_de_datos():

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

        self.cursor.execute("INSERT INTO COCTELES VALUES (NULL,?,?)",cocktail)
        self.cocktails.commit()

    def remove_cocktail(self,cocktail):

        orden="DELETE FROM COCTELES WHERE COCKTAIL='"+cocktail+"'"
        self.cursor.execute(orden)
        self.cocktails.commit()

    def seeAll(self):

        self.cursor.execute("SELECT *FROM COCTELES")

        return self.cursor.fetchall()