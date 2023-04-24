'''
Michelle Luo
Cmdr. Schenk
AP Computer Science
Master Project Database (cryptodatabase.py)
Spring of 2023
'''

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
                return 1
            return 0

    def checkPassword(self, username, password):
        self.cursor.execute("SELECT id_account FROM account WHERE username='{}' AND password='{}'".format(username, password))
        resultList=self.cursor.fetchall()
        try:
            resultTuple=resultList[0]
            id_password=resultTuple[0]
            return id_password
        except:
            return "incorrect password"

    def startAccount(self, email, username, password):
        #FIX: input INSERT INTO SQL statement and such
        self.cursor.execute("SELECT id_account FROM account WHERE username='{}'".format(username))
        resultList=self.cursor.fetchall()
        if len(resultList)!=0:
            return "Account taken"
        else:
            thingy="INSERT INTO account (email, username, password) VALUES ('{}','{}','{}');".format(email,username,password)
            self.cursor.execute(thingy)
            self.connection.commit()
            result=self.cursor.fetchall()

    def insertCryptoDB(self, cryptoID,plainText,cipherText,user1,user2,userID):
        if user1=="NULL":
            user1=None
        if user2=="NULL":
            user2=None
        if user1==None:
            insertQ="INSERT INTO encrypt (id_total_encrypt, id_user_encrypt, plain_text, cipher_text) VALUES ('{}','{}','{}','{}');".format(cryptoID,userID,plainText,cipherText)
            self.cursor.execute(insertQ)
            self.connection.commit()
            result=self.cursor.fetchall()
        elif user2==None:
            insertQ="INSERT INTO encrypt (id_total_encrypt, id_user_encrypt, plain_text, cipher_text, encryption_type) VALUES ('{}','{}','{}','{}','{}');".format(cryptoID,userID,plainText,cipherText,user1)
            self.cursor.execute(insertQ)
            self.connection.commit()
            result=self.cursor.fetchall()
        else:
            insertQ="INSERT INTO encrypt (id_total_encrypt, id_user_encrypt, plain_text, cipher_text, encryption_type, encryption_type2) VALUES ('{}','{}','{}','{}','{}','{}');".format(cryptoID,userID,plainText,cipherText,user1,user2)
            self.cursor.execute(insertQ)
            self.connection.commit()
            result=self.cursor.fetchall()

    def updateCryptoDB(self, cryptoID,plainText,cipherText,user1,user2,userID):

        if user1=="NULL":
            user1=None
        if user2=="NULL":
            user2=None
        if user1==None:
            updateQ="UPDATE encrypt SET plain_text='{}', cipher_text='{}' WHERE id_user_encrypt={} AND id_total_encrypt='{}';".format(plainText, cipherText, userID, cryptoID)
            self.cursor.execute(updateQ)
            self.connection.commit()
            result=self.cursor.fetchall()
        elif user2==None:
            updateQ="UPDATE encrypt SET plain_text='{}', cipher_text='{}', encryption_type='{}' WHERE id_user_encrypt={} AND id_total_encrypt='{}';".format(plainText, cipherText, user1, userID, cryptoID)            
            self.cursor.execute(updateQ)
            self.connection.commit()
            result=self.cursor.fetchall()
        else:
            updateQ="UPDATE encrypt SET plain_text='{}', cipher_text='{}', encryption_type='{}', encryption_type2='{}' WHERE id_user_encrypt={} AND id_total_encrypt='{}';".format(plainText, cipherText, user1, user2, userID, cryptoID)            
            self.cursor.execute(updateQ)
            self.connection.commit()
            result=self.cursor.fetchall()

    def deleteCryptoDB(self, cryptoID, userID):
        deleteQ="DELETE FROM encrypt WHERE id_total_encrypt={} AND id_user_encrypt={}".format(cryptoID,userID)
        self.cursor.execute(deleteQ)
        self.connection.commit()
        result=self.cursor.fetchall()

    def goToEntry(self, entryNumber,userID):
        #FIX:
        selectQ="SELECT * FROM encrypt WHERE id_user_encrypt={} AND id_total_encrypt={}".format(userID, entryNumber)
        self.cursor.execute(selectQ)
        listResult=self.cursor.fetchall()
        tupleResult=listResult[0]
        return tupleResult

    def findMaxLength(self, userID):
        maxQuery="SELECT * FROM encrypt WHERE id_user_encrypt={} ORDER BY id_total_encrypt DESC".format(userID)
        self.cursor.execute(maxQuery)
        listResult=self.cursor.fetchall()
        if listResult==[]:
            finalID=0
            return finalID
        tupleResult=listResult[0]
        finalID=tupleResult[1]
        return finalID