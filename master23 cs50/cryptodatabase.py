'''
Michelle Luo
Cmdr. Schenk
AP Computer Science
Master Project Database
Spring of 2023
'''
#DONT FORGET TO DELETE ALL <DB> ERROR TAGS WITH FINAL SUBMISSION
#imports
import mysql.connector

#FIX: marks where everything is

class CryptoDatabase:
    #__init__ method
    def __init__(self):
        self.connect=False

    #open connection method
    def setConnection(self):
        if (self.connect == False):
            try:
                self.connection = mysql.connector.connect(
                #connection to localhost at 127.0.0.1
                host = "localhost",
                user = "root",
                password = "!@#seojean_and_sam90",
                database = "crypto"

                #connection at jchs :D
                #host="192.168.0.116"
                #user="leia"
                #password="jchs"
                #database="crypto"
                )
                self.cursor = self.connection.cursor()
                self.connect=True	
            except:
                print("Error occured while opening the connection. <DB>")
                return 1  
            return 0
    
    #close connection method
    def breakConnection(self):
        if (self.connect == True):
            try:
                self.cursor.close()
                self.connection.close()
                self.connect=False
            except:
                print("Error occured while closing the connection. <DB>")
                return 1
            return 0

    def checkPassword(self, username, password):
        self.cursor.execute("SELECT id_password FROM password WHERE username='{}' AND password='{}'".format(username, password))
        resultList=self.cursor.fetchall()
        try:
            resultTuple=resultList[0]
            id_password=resultTuple[0]
            return id_password
        except:
            return "incorrect password"

    def startAccount(self, email, username, password):
        #FIX: input INSERT INTO SQL statement and such
        self.cursor.execute("SELECT id_password FROM password WHERE username='{}'".format(username))
        resultList=self.cursor.fetchall()
        if len(resultList)!=0:
            return "Account taken"
        else:
            thingy="INSERT INTO password (email, username, password) VALUES ('{}','{}','{}');".format(email,username,password)
            self.cursor.execute(thingy)
            self.connection.commit()
            result=self.cursor.fetchall()
