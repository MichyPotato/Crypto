'''
Michelle Luo
Cmdr. Schenk
AP Computer Science
Master Project Encryption methods (encryption.py)
Spring of 2023
'''

#imports
from base64 import b32encode

#Encryption class
class Encryption:

    #function for 
    def caesar(self, plainText, key):
        cipherText=""
        # traverse text
        for i in range(len(plainText)):
            char = plainText[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                cipherText+= chr((ord(char) + key-65) % 26 + 65)
            # Encrypt lowercase characters
            elif (char==" "):
                cipherText+=char
            else:
                cipherText += chr((ord(char) + key - 97) % 26 + 97)
        return cipherText
    def bookCipher(self, plainText, bookFileAddress):
        self.cipherTextList=[]
        self.linePosition=0
        self.wordPosition=0
        self.plainTextList=plainText.split(" ")
        for stringWord in self.plainTextList:
            self.finalPosition=self.bcFindWord(stringWord, bookFileAddress)
            if self.finalPosition=="NOT A WORD FOUND":
                self.cipherTextList.append(stringWord)
            else:
                self.cipherTextList.append(self.finalPosition)
        self.cipherText=" ".join(self.cipherTextList)
        return self.cipherText
    def bcFindWord(self, stringWord, bookFileAddress):
        with open(bookFileAddress, encoding='utf-8') as myBookFile: 
            self.linePosition=0
            for bookLine in myBookFile: 
                self.linePosition+=1
                self.wordPosition=0
                wordList=bookLine.split(" ") 
                for bookWord in wordList: 
                    self.wordPosition+=1
                    if (bookWord==stringWord): 
                        self.finalPosition=str(self.linePosition)+"."+str(self.wordPosition) 
                        return self.finalPosition
                    else:
                        continue
        return "NOT A WORD FOUND"
    def hexString(self, plainText):
        cipherText=plainText.encode().hex()
        return cipherText
    def b32(self, plainText):
        cipherText=b32encode(plainText.encode())
        return cipherText