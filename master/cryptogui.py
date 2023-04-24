'''
Michelle Luo
Cmdr. Schenk
AP Computer Science
Master Project GUI (cryptogui.py)
Spring of 2023
'''

#imports
from cryptodatabase import CryptoDatabase
from encryption import Encryption
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

class CryptoGUI:

    def __init__(self):
        #uniform variables for text color and font [the s stands for standard]
        self.textColor= "#00cc00"
        self.sFont= "Terminal"
        self.userMessage=""
        self.isEncryptButton="False"
        self.recentSelection1=""
        self.fileName=""
        self.userChoice1=""
        self.userChoice2=""
        self.userID=0
        self.entryNumber=0
        #define connection and instantiation of the database file
        self.db=CryptoDatabase()
        self.encrypt=Encryption()
        self.db.setConnection()
        #processes to run
        self.createLoginWindow()
        self.createLoginMenu()
        self.createLoginButtons()
        #self.createCryptoButtons()
        self.loginWindow.mainloop()
    
    def createLoginWindow(self):
        #define the loginWindow and its attributes
        self.loginWindow=tk.Tk()
        self.loginWindow.title("Login")
        self.loginWindow.geometry("1280x600")
        self.loginWindow['bg']="black"
        self.loginWindow.attributes('-fullscreen',True)
        self.logo = Image.open("logo.png")
        self.logo = self.logo.resize((256, 120), Image.ANTIALIAS)
        self.lPic = ImageTk.PhotoImage(self.logo)
        self.lMyPic = tk.Label(self.loginWindow, image=self.lPic, bg="black")
        self.lMyPic.place(x = 50, y = 10)

    def createLoginMenu(self):
        #menu system initiated
        self.menubar= tk.Menu(self.loginWindow)
        self.loginWindow.config(menu= self.menubar)
        self.fileMenu = tk.Menu(self.menubar, tearoff = 0)
        self.fileMenu.add_command(label = "Exit", font = (self.sFont, 18), foreground = (self.textColor), command = self.loginWindow.destroy)
        self.menubar.add_cascade(label = "File", font = (self.sFont, 18), foreground = (self.textColor), menu = self.fileMenu)
        self.helpMenu = tk.Menu(self.menubar, tearoff = 0)
        self.helpMenu.add_command(label="About",font = (self.sFont, 18), foreground = (self.textColor), command = self.aboutWindow)
        self.menubar.add_cascade(label = "Help", font = (self.sFont, 18), foreground = (self.textColor), menu = self.helpMenu)

    def createLoginButtons(self):
        #define buttons
        self.exitButton=tk.Button(self.loginWindow, text="Exit", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.destroyWindow)
        self.aboutButton=tk.Button(self.loginWindow, text = "About", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.aboutWindow)
        self.helpButton=tk.Button(self.loginWindow, text = "Help", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.helpWindow)
        self.loginButton=tk.Button(self.loginWindow, text = "LOGIN", font=(self.sFont, 20), fg=(self.textColor), bg=("black"),command=self.login)
        self.startSignupButton=tk.Button(self.loginWindow, text = "If you do not have a Crypto account, sign up today!", font=(self.sFont, 12), fg=(self.textColor), borderwidth= 0,bg=("black"),command=self.openSignup)
        #place buttons
        self.exitButton.place(x=325,y=50)
        self.aboutButton.place(x=415,y=50)
        self.helpButton.place(x=525,y=50)
        self.loginButton.place(x=590,y=400)
        self.startSignupButton.place(x=350,y=580)
        #define labels
        self.usernameLabel=tk.Label(self.loginWindow,text="Username",font=(self.sFont, 18), bg=("black"), fg=(self.textColor))
        self.passwordLabel=tk.Label(self.loginWindow,text="Password",font=(self.sFont, 18), bg=("black"), fg=(self.textColor))
        self.userMessageLabel=tk.Label(self.loginWindow,text=self.userMessage,font=(self.sFont, 12), bg=("black"), fg=("#ff3300"))
        #define Text fields
        self.usernameEntry=tk.Entry(self.loginWindow, font=(self.sFont, 18), relief= "sunken")
        self.passwordEntry=tk.Entry(self.loginWindow, font=(self.sFont, 18), relief= "sunken", show="*")
        #place labels
        self.usernameLabel.place(x=480,y=200)
        self.passwordLabel.place(x=480,y=300)
        self.userMessageLabel.place(x=505,y=170)
        #place text fields
        self.usernameEntry.place(x=480,y=250)
        self.passwordEntry.place(x=480,y=350)

    def createSignupButtons(self):
        #define signup buttons
        self.backButton=tk.Button(self.loginWindow, text="Back", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.openLoginFromSU)
        self.aboutButton=tk.Button(self.loginWindow, text = "About", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.aboutWindow)
        self.helpButton=tk.Button(self.loginWindow, text = "Help", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.helpWindow)
        self.signupButton=tk.Button(self.loginWindow, text="Sign Up", font = (self.sFont, 20), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.signup)
        #define signup labels
        self.signupLabel=tk.Label(self.loginWindow, text="Crypto Account Sign Up", font=(self.sFont, 20), bg=("black"), fg=(self.textColor))
        self.emailSULabel=tk.Label(self.loginWindow, text="Email", font=(self.sFont, 14), bg=("black"), fg=(self.textColor))
        self.newUsernameSULabel=tk.Label(self.loginWindow, text="Enter your Username below", font=(self.sFont, 14), bg=("black"), fg=(self.textColor))
        self.newPasswordSULabel=tk.Label(self.loginWindow, text="Enter your Password below", font=(self.sFont, 14), bg=("black"), fg=(self.textColor))
        self.userMessageLabel=tk.Label(self.loginWindow,text=self.userMessage,font=(self.sFont, 12), bg=("black"), fg=("#ff3300"))
        #define signup entries
        self.emailSUEntry=tk.Entry(self.loginWindow, font=(self.sFont, 18), relief= "sunken")
        self.usernameSUEntry=tk.Entry(self.loginWindow, font=(self.sFont, 18), relief= "sunken")
        self.PasswordSUEntry=tk.Entry(self.loginWindow, font=(self.sFont, 18), relief= "sunken", show="*")  
        #place signup buttons 
        self.backButton.place(x=325,y=50)
        self.aboutButton.place(x=415,y=50)
        self.helpButton.place(x=525,y=50) 
        self.signupButton.place(x=540,y=500)
        #place signup labels
        self.signupLabel.place(x=440,y=150)
        self.emailSULabel.place(x=450,y=200)
        self.newUsernameSULabel.place(x=450,y=300)
        self.newPasswordSULabel.place(x=450,y=400)
        self.userMessageLabel.place(x=430,y=180)
        #place signup entries
        self.emailSUEntry.place(x=450,y=250)
        self.usernameSUEntry.place(x=450,y=350)
        self.PasswordSUEntry.place(x=450,y=450)

        self.bgPic = Image.open("hacka.png")
        #self.bgPic = self.bgPic.resize((512, 226), Image.ANTIALIAS)
        self.bPic = ImageTk.PhotoImage(self.bgPic)
        self.bMyPic = tk.Label(self.loginWindow, image=self.bPic, bg="black")
        self.bMyPic.place(x = 850, y = 200)

        self.bg2Pic = Image.open("computa.png")
        self.bg2Pic = self.bg2Pic.resize((402, 236), Image.ANTIALIAS)
        self.b2Pic = ImageTk.PhotoImage(self.bg2Pic)
        self.b2MyPic = tk.Label(self.loginWindow, image=self.b2Pic, bg="black")
        self.b2MyPic.place(x = 0, y = 230)

    def createCryptoButtons(self):
        self.backButton=tk.Button(self.loginWindow, text="Back", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.openLoginFromCrypto)
        self.backButton.place(x=325,y=50)
        #define self.idText
        self.idText=""
        #GUI fields' labels, text fields,etc
        #create labels:
        self.userMessageLabel=tk.Label(self.loginWindow,text=self.userMessage,font=(self.sFont, 12), bg=("black"), fg=("#ff3300"))
        self.idLabel=tk.Label(self.loginWindow, text="Encryption Number", font=(self.sFont, 18), bg=("black"), fg=(self.textColor))
        self.idText=tk.Label(self.loginWindow, text=self.idText, font=(self.sFont, 18), bg=("black"), fg=(self.textColor))
        self.plainTextLabel=tk.Label(self.loginWindow, text="Plain Text", font=(self.sFont, 18), bg=("black"), fg=(self.textColor))
        self.cipherTextLabel=tk.Label(self.loginWindow, text="Cipher Text", font=(self.sFont, 18), bg=("black"), fg=(self.textColor), state="disabled")
        self.encryptionSectionLabel=tk.Label(self.loginWindow, text="Encryption Options", font=(self.sFont, 20), bg=("black"), fg=(self.textColor))
        #place labels
        self.userMessageLabel.place(x=400,y=250)
        self.idLabel.place(x=54,y=200)
        self.idText.place(x=350,y=200)
        self.plainTextLabel.place(x=50,y=300)
        self.cipherTextLabel.place(x=500, y=300)
        self.encryptionSectionLabel.place(x=950,y= 75)

        self.plainTextFrame = tk.Frame(self.loginWindow, width = 380, height = 245)
        self.cipherTextFrame = tk.Frame(self.loginWindow, width = 380, height = 245)

        self.plainTextFrame.place(x = 50, y = 350)
        self.cipherTextFrame.place( x= 500, y = 350)

        #create text fields:
        self.plainTextField=scrolledtext.ScrolledText(self.plainTextFrame, font=(self.sFont, 12), height=15, width=30, wrap=tk.WORD)
        self.cipherTextField=scrolledtext.ScrolledText(self.cipherTextFrame, font=(self.sFont, 12), height=15, width=30, wrap=tk.WORD)
        self.cipherTextField["state"]="disabled"
        #place text fields
        self.plainTextField.place(x=0,y=0)
        self.cipherTextField.place(x=0,y=0)


        #CRUD Buttons for GUI
        #create buttons
        self.insertButton=tk.Button(self.loginWindow, text="Save New Message", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.insertCryptoGUI)
        self.updateButton=tk.Button(self.loginWindow, text="Save Changes", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.updateCryptoGUI)
        self.deleteButton=tk.Button(self.loginWindow, text="Delete a Message", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.deleteCryptoGUI)
        self.backAllButton=tk.Button(self.loginWindow, text="|<<", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.backAllCryptoGUI)
        self.back2Button=tk.Button(self.loginWindow, text="<<", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.back2CryptoGUI)
        self.back1Button=tk.Button(self.loginWindow, text="<", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.back1CryptoGUI)
        self.forward1Button=tk.Button(self.loginWindow, text=">", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.forward1CryptoGUI)
        self.forward2Button=tk.Button(self.loginWindow, text=">>", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.forward2CryptoGUI)
        self.forwardAllButton=tk.Button(self.loginWindow, text=">>|", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.forwardAllCryptoGUI)
        #place buttons
        self.insertButton.place(x=600,y=50)
        self.updateButton.place(x=600,y=100)
        self.deleteButton.place(x=600,y=150)
        self.backAllButton.place(x=200,y=600)
        self.back2Button.place(x=300,y=600)
        self.back1Button.place(x=400,y=600)
        self.forward1Button.place(x=500,y=600)
        self.forward2Button.place(x=600,y=600)
        self.forwardAllButton.place(x=700,y=600)

        #line Image to seperate Text Fields with the Encryption Fields on GUI
        self.bgPic = Image.open("greenLine.png")
        self.bgPic = self.bgPic.resize((30, 600), Image.ANTIALIAS)
        self.bPic = ImageTk.PhotoImage(self.bgPic)
        self.bMyPic = tk.Label(self.loginWindow, image=self.bPic, bg="black")
        self.bMyPic.place(x = 900, y = 50)

        #all SPECIFICALLY encryption selection buttons, labels, etc.
        #ComboBox 1's LABEL
        self.firstEncryptionLabel=tk.Label(self.loginWindow, text="Encryption Method:", font=(self.sFont, 14), bg=("black"), fg=(self.textColor))
        #place label
        self.firstEncryptionLabel.place(x=950,y=150)
        # ComboBox 1 for choosing method of encryption
        #list of encryption options 1
        self.optionsList1 = ["Caesar Cipher", "Base32", "Hex", "Book Cipher"]
        #set a StringVar object in the window
        self.firstEncryptionOptionValue = tk.StringVar(self.loginWindow,'')
        #default value for encryption options 1
        self.firstEncryptionOptionValue.set("Choose Encryption Method")
        #establish combobox for choosing encryption 1
        self.firstEncryptionOptionMenu = ttk.Combobox(self.loginWindow, textvariable=  self.firstEncryptionOptionValue, state = 'readonly', foreground = "grey", font = (self.sFont, 16),width = 25, values = self.optionsList1)
        #place the combobox 1
        self.firstEncryptionOptionMenu.place(x=950,y=200)
        #if the combobox value is ever changed, call upon the function self.checkEncryptionResult1
        self.firstEncryptionOptionValue.trace_add("write", self.checkEncryptionResult1)

    def checkEncryptionResult1(self,var,index,mode):
        #if the previous selection was a caesar cipher or book cipher, meaning extra GUI parts, delete the GUI parts.
        if self.recentSelection1=="Caesar Cipher":
            self.secondEncryptionLabel.destroy()
            self.secondEncryptionOptionMenu.destroy()
            if self.isEncryptButton=="True":
                self.encryptButton.destroy()
                self.isEncryptButton="False"
        elif self.recentSelection1=="Book Cipher":
            self.fileUploadLabel.destroy()
            self.fileUploadButton.destroy()
        #destroy the encrypt button if it is there from a previous selection
        elif self.isEncryptButton=="True":
            self.encryptButton.destroy()
            self.isEncryptButton="False"
        #get the user choice for combobox1
        self.userChoice1=self.firstEncryptionOptionMenu.get()
        #if the user chose caesar cipher, run this
        if self.userChoice1=="Caesar Cipher":
            self.recentSelection1="Caesar Cipher"
            self.secondEncryptionValueStart()
        #if the user chose book cipher, run this
        elif self.userChoice1=="Book Cipher":
            self.recentSelection1="Book Cipher"
            self.secondEncryptionValueStart()
        #if the user chose Base 32 or hex, run this
        elif self.userChoice1=="Base32":
            self.recentSelection1="Base32"
            self.encryptButton=tk.Button(self.loginWindow, text="ENCRYPT MESSAGE", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.encryptGUI)
            self.encryptButton.place(x=950,y=250)
            self.isEncryptButton="True"
        elif self.userChoice1=="Hex":
            self.recentSelection1="Hex"
            self.encryptButton=tk.Button(self.loginWindow, text="ENCRYPT MESSAGE", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.encryptGUI)
            self.encryptButton.place(x=950,y=250)
            self.isEncryptButton="True"

    def postNavigationEncryptionSetUp(self):
        #if the previous selection was a caesar cipher or book cipher, meaning extra GUI parts, delete the GUI parts.
        if self.recentSelection1=="Caesar Cipher":
            self.secondEncryptionLabel.destroy()
            self.secondEncryptionOptionMenu.destroy()
            if self.isEncryptButton=="True":
                self.encryptButton.destroy()
                self.isEncryptButton="False"
        elif self.recentSelection1=="Book Cipher":
            self.fileUploadLabel.destroy()
            self.fileUploadButton.destroy()
        #destroy the encrypt button if it is there from a previous selection
        elif self.isEncryptButton=="True":
            self.encryptButton.destroy()
            self.isEncryptButton="False"
        #get the user choice for combobox1
        self.userChoice1=self.firstEncryptionOptionMenu.get()
        #if the user chose caesar cipher, run this
        if self.userChoice1=="Caesar Cipher":
            self.recentSelection1="Caesar Cipher"
            self.secondEncryptionValueStart()
            self.secondEncryptionOptionValue.set(self.tupleResult[6])
        #if the user chose book cipher, run this
        elif self.userChoice1=="Book Cipher":
            self.recentSelection1="Book Cipher"
            self.secondEncryptionValueStart()
        #if the user chose Base 32 or hex, run this
        elif self.userChoice1=="Base32":
            self.recentSelection1="Base32"
            self.encryptButton=tk.Button(self.loginWindow, text="ENCRYPT MESSAGE", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.encryptGUI)
            self.encryptButton.place(x=950,y=250)
            self.isEncryptButton="True"
        elif self.userChoice1=="Hex":
            self.recentSelection1="Hex"
            self.encryptButton=tk.Button(self.loginWindow, text="ENCRYPT MESSAGE", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.encryptGUI)
            self.encryptButton.place(x=950,y=250)
            self.isEncryptButton="True" 
        elif self.userChoice1=="Choose Encryption Method":
            self.recentSelection1=""

    def checkEncryptionResult2(self,var,index,mode):
        self.encryptButton=tk.Button(self.loginWindow, text="ENCRYPT MESSAGE", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.encryptGUI)
        self.encryptButton.place(x=950,y=350)
        self.isEncryptButton="True"

    def encryptGUI(self):
        self.cipherText=""
        self.userChoice1=self.firstEncryptionOptionMenu.get()
        self.plainText=self.plainTextField.get("1.0",'end-1c')

        if self.plainText=="":
            self.userMessage="No text to encode in Plain Text"
            self.userMessageLabel.config(text=self.userMessage)
            self.userMessageLabel.after(3000, self.hideUserMessage)
        elif self.userChoice1=="Caesar Cipher":
            self.userChoice2=int(self.secondEncryptionOptionMenu.get())
            self.cipherText=self.encrypt.caesar(self.plainText, self.userChoice2)
        elif self.userChoice1=="Hex":
            self.cipherText=self.encrypt.hexString(self.plainText)
        elif self.userChoice1=="Base32":
            self.cipherText=self.encrypt.b32(self.plainText)
        elif self.userChoice1=="Book Cipher" and self.plainText!="" and self.fileName!="":
            self.cipherText=self.encrypt.bookCipher(self.plainText,self.fileName)
        elif self.userChoice1=="Book Cipher" and self.fileName=="":
            self.userMessage="No Book File to encode using B-Cipher"
            self.userMessageLabel.config(text=self.userMessage)
            self.userMessageLabel.after(3000, self.hideUserMessage)
        else:
            self.userMessage="Some error occured: please try again."
            self.userMessageLabel.config(text=self.userMessage)
            self.userMessageLabel.after(3000, self.hideUserMessage)
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0",'end')
        self.cipherTextField.insert("end",self.cipherText)
        self.cipherTextField["state"]="disabled"
    
    def secondEncryptionValueStart(self):
        if self.userChoice1=="Caesar Cipher":
            #ComboBox 2's LABEL
            self.secondEncryptionLabel=tk.Label(self.loginWindow, text="Rotate by:", font=(self.sFont, 14), bg=("black"), fg=(self.textColor))
            #place label
            self.secondEncryptionLabel.place(x=950,y=250)
            # ComboBox 2 for choosing method of encryption
            #list of encryption options 2
            self.optionsList2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
            #set a StringVar object in the window
            self.secondEncryptionOptionValue = tk.StringVar(self.loginWindow,'')
            #default value for encryption options 2
            self.secondEncryptionOptionValue.set("Choose Rotation Key")
            #establish combobox for choosing encryption 2
            self.secondEncryptionOptionMenu = ttk.Combobox(self.loginWindow, textvariable=self.secondEncryptionOptionValue, state = 'readonly', foreground = "grey", font = (self.sFont, 16),width = 25, values = self.optionsList2)
            #place the combobox 2
            self.secondEncryptionOptionMenu.place(x=950,y=300)
            #if the combobox value is ever changed, call upon the function self.checkEncryptionResult2
            self.secondEncryptionOptionValue.trace_add("write", self.checkEncryptionResult2)

        elif self.userChoice1=="Book Cipher":
            #
            self.fileUploadLabel=tk.Label(self.loginWindow, text="Upload a Text File of a Book", font=(self.sFont, 14), bg=("black"), fg=(self.textColor))
            self.fileUploadLabel.place(x=950,y=250)
            self.fileUploadButton = tk.Button(self.loginWindow, text='Text File Upload', command=self.uploadFile, font=(self.sFont, 14))
            self.fileUploadButton.place(x=1000,y=300)

    def uploadFile(self,event=None):
        #define the various file types that are used
        fileTypes = (('text files', '*.txt'),('All files', '*.*'))
        #create a dialog that prompts for a text file
        self.fileName = filedialog.askopenfilename(title="Open a Text File", initialdir="/",filetypes=fileTypes)
        if self.fileName=="":
            self.userMessage="No File selected"
            self.userMessageLabel.config(text=self.userMessage)
            self.userMessageLabel.after(3000, self.hideUserMessage)
            return []
        #establishes encrypt button after file is uploaded?
        self.encryptButton=tk.Button(self.loginWindow, text="ENCRYPT MESSAGE", font = (self.sFont, 18), borderwidth= 0, fg = (self.textColor), bg=("black"), command=self.encryptGUI)
        self.encryptButton.place(x=950,y=350)
        self.isEncryptButton="True"

    def destroyLoginButtons(self):
        #destroy all of the login buttons, labels, entries on screem
        self.exitButton.destroy()
        self.loginButton.destroy()
        self.startSignupButton.destroy()
        self.usernameLabel.destroy()
        self.passwordLabel.destroy()
        self.userMessageLabel.destroy()
        self.usernameEntry.destroy()
        self.passwordEntry.destroy()
        self.aboutButton.destroy()
        self.helpButton.destroy()

    def destroySignupButtons(self):
        self.backButton.destroy()
        self.signupButton.destroy()    
        self.signupLabel.destroy()
        self.emailSULabel.destroy()  
        self.newUsernameSULabel.destroy()  
        self.newPasswordSULabel.destroy()  
        self.emailSUEntry.destroy()  
        self.usernameSUEntry.destroy()  
        self.PasswordSUEntry.destroy()  
        self.userMessageLabel.destroy()
        self.aboutButton.destroy()
        self.helpButton.destroy()
        self.b2MyPic.destroy()
        self.bMyPic.destroy()

    def destroyCryptoButtons(self):
        self.userMessage=""
        self.backButton.destroy()
        self.userMessageLabel.destroy()
        self.idLabel.destroy()
        self.idText.destroy()
        self.plainTextLabel.destroy()
        self.cipherTextLabel.destroy()
        self.encryptionSectionLabel.destroy()
        self.plainTextFrame.destroy()
        self.cipherTextFrame.destroy()
        self.insertButton.destroy()
        self.updateButton.destroy()
        self.deleteButton.destroy()
        self.backAllButton.destroy()
        self.back2Button.destroy()
        self.back1Button.destroy()
        self.forward1Button.destroy()
        self.forward2Button.destroy()
        self.forwardAllButton.destroy()
        self.bMyPic.destroy()
        self.firstEncryptionLabel.destroy()
        self.firstEncryptionOptionMenu.destroy()
        if self.userChoice1=="Caesar Cipher":
            self.secondEncryptionLabel.destroy()
            self.secondEncryptionOptionMenu.destroy()
        if self.userChoice1=="Book Cipher":
            self.fileUploadLabel.destroy()
            self.fileUploadButton.destroy()
        if self.isEncryptButton=="True":
            self.encryptButton.destroy()
            self.isEncryptButton="False"

    def destroyWindow(self):
        #destroy/exit out the window
        self.loginWindow.destroy()

    def aboutWindow(self):
        messagebox.showinfo(title="About Crypto",
                            message="Crypto (short for Cryptography's Really Your Power To Own) is a database cryptographic encryption system developed by Michelle Luo.",
                            detail="This app allows you to encode messages and save them to your user specific account. Only YOU can access your saved encrypted messages.",
                            icon=messagebox.INFO
                            )

    def helpWindow(self):
        messagebox.showinfo(title="Basic Navigation of Crypto",
                            message="1. Sign Up for an Account \n2. Login with your Account \n3. Input your message in the PLAIN TEXT section,\n then choose an encryption method on the right.\n4. Once you are done filling out the encryption options, click ENCRYPT. \n5. You should now see an encrypted section of text in the CIPHER TEXT Field.",
                            detail="For more detailed instructions, please actually pay attention to Michelle Luo in her Master Project Presentation. :D",
                            icon=messagebox.INFO
                            )

    def hideUserMessage(self):
        #hide the user warning message on screen
        self.userMessage=""
        self.userMessageLabel.config(text=self.userMessage)

    def login(self):
        #gets user inputted username and password
        username=self.usernameEntry.get()
        password=self.passwordEntry.get()
        #sends it for a check through the checkPassword() in cryptodatabase.py
        self.loginResult=self.db.checkPassword(username, password)
        #if the credentials were incorrect, send a message to the user on screen
        if self.loginResult=="incorrect password":
            self.userMessage="Incorrect Credentials!"
            self.userMessageLabel.config(text=self.userMessage)
            #the user message disappears after 3 seconds
            self.userMessageLabel.after(3000, self.hideUserMessage)
        else:
            #if the credentials are right, open the crypto server with the password_id in the server
            self.userID=self.loginResult
            self.openCrypto()

    def signup(self):
        #gets user inputted email, username, and password
        email=self.emailSUEntry.get()
        username=self.usernameSUEntry.get()
        password=self.PasswordSUEntry.get()
        signupResult=self.db.startAccount(email,username,password)
        if signupResult=="Account taken":
            self.userMessage="This Username is already taken!"
            self.userMessageLabel.config(text=self.userMessage)
            #the user message disappears after 3 seconds
            self.userMessageLabel.after(3000, self.hideUserMessage)
        else:
            self.destroySignupButtons()
            self.createLoginButtons()

    def openLoginFromSU(self):
        #destroy the sign up GUI
        self.destroySignupButtons()
        #change window title to login
        self.loginWindow.title("Login")
        #implement login GUI buttons
        self.createLoginButtons()

    def openLoginFromCrypto(self):
        #destroy crypto GUI
        self.destroyCryptoButtons()
         #change window title to login
        self.loginWindow.title("Login")
        #implement login GUI buttons
        self.createLoginButtons()

    def openSignup(self):
        #destroy the login GUI
        self.destroyLoginButtons()
        #change window title to signup
        self.loginWindow.title("Sign Up")
        #implement signup GUI buttons
        self.createSignupButtons()

    def openCrypto(self):
        #destroy the login GUI
        self.destroyLoginButtons()
        #change window title to Crypto
        self.loginWindow.title("Crypto")
        self.createCryptoButtons()
        
    def insertCryptoGUI(self):
        newCryptoID=self.db.findMaxLength(self.userID)+1
        user1="NULL"
        user2="NULL"
        #something for the id label
        plainText=self.plainTextField.get("1.0", tk.END)
        cipherText=self.cipherTextField.get("1.0", tk.END)
        if self.userChoice1=="Caesar Cipher":
            user1="caesar"
            user2=self.secondEncryptionOptionMenu.get()
        elif self.userChoice1=="Book Cipher":
            user1="book"
            user2=self.fileName
        elif self.userChoice1=="Hex":
            user1="hex"
        elif self.userChoice1=="Base32":
            user1="base"
        elif self.userChoice1=="":
            user1="NULL"
            user2="NULL"
        else:
            pass
        self.db.insertCryptoDB(newCryptoID,plainText,cipherText,user1,user2,self.userID)

    def updateCryptoGUI(self):
        user1="NULL"
        user2="NULL"
        #something for the id label
        plainText=self.plainTextField.get("1.0", tk.END)
        cipherText=self.cipherTextField.get("1.0", tk.END)
        if self.userChoice1=="Caesar Cipher":
            user1="caesar"
            user2=self.secondEncryptionOptionMenu.get()
        elif self.userChoice1=="Book Cipher":
            user1="book"
            user2=self.fileName
        elif self.userChoice1=="Hex":
            user1="hex"
        elif self.userChoice1=="Base32":
            user1="base"
        elif self.userChoice1=="":
            user2="NULL"
        else:
            pass
        self.db.updateCryptoDB(self.entryNumber,plainText,cipherText,user1,user2,self.userID)

    def deleteCryptoGUI(self):
        if self.entryNumber != 0:
            userPromptDelete=messagebox.askyesno("WARNING", "Do you really want to delete this record?")
            if userPromptDelete == True:
                self.db.deleteCryptoDB(self.entryNumber, self.userID)
                self.entryNumber=0
                self.idText.configure(text="")
                self.plainTextField.delete("1.0","end")
                self.cipherTextField["state"]="normal"
                self.cipherTextField.delete("1.0","end")
                self.cipherTextField["state"]="disabled"
                self.firstEncryptionOptionValue.set("Choose Encryption Method")
                self.postNavigationEncryptionSetUp()
            else:
                self.userMessage="Did not delete"
                self.userMessageLabel.config(text=self.userMessage)
                #the user message disappears after 3 seconds
                self.userMessageLabel.after(3000, self.hideUserMessage)
        else:
            self.userMessage="Cannot delete a non-existent Entry"
            self.userMessageLabel.config(text=self.userMessage)
            #the user message disappears after 3 seconds
            self.userMessageLabel.after(3000, self.hideUserMessage)

    def backAllCryptoGUI(self):
        self.tupleResult=self.db.goToEntry(1, self.userID)

        self.entryNumber=self.tupleResult[1]
        self.idText.configure(text=str(self.entryNumber))
        self.plainTextField.delete("1.0","end")
        self.plainTextField.insert("end", self.tupleResult[3])
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0","end")
        self.cipherTextField.insert("end", self.tupleResult[4])
        self.cipherTextField["state"]="disabled"
        if self.tupleResult[5]=="caesar":
            self.firstEncryptionOptionValue.set("Caesar Cipher")
        elif self.tupleResult[5]=="hex":
            self.firstEncryptionOptionValue.set("Hex")
        elif self.tupleResult[5]=="base":
            self.firstEncryptionOptionValue.set("Base32")
        elif self.tupleResult[5]=="book":
            self.fileName=self.tupleResult[6]
            self.firstEncryptionOptionValue.set("Book Cipher")
        self.postNavigationEncryptionSetUp()

    def back2CryptoGUI(self):
        self.entryNumber=self.entryNumber-2
        if self.entryNumber<1:
            self.entryNumber=1
        self.tupleResult=self.db.goToEntry(self.entryNumber, self.userID)

        self.entryNumber=self.tupleResult[1]
        self.idText.configure(text=str(self.entryNumber))
        self.plainTextField.delete("1.0","end")
        self.plainTextField.insert("end", self.tupleResult[3])
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0","end")
        self.cipherTextField.insert("end", self.tupleResult[4])
        self.cipherTextField["state"]="disabled"
        if self.tupleResult[5]=="caesar":
            self.firstEncryptionOptionValue.set("Caesar Cipher")
        elif self.tupleResult[5]=="hex":
            self.firstEncryptionOptionValue.set("Hex")
        elif self.tupleResult[5]=="base":
            self.firstEncryptionOptionValue.set("Base32")
        elif self.tupleResult[5]=="book":
            self.fileName=self.tupleResult[6]
            self.firstEncryptionOptionValue.set("Book Cipher")
        self.postNavigationEncryptionSetUp()

    def back1CryptoGUI(self):
        self.entryNumber=self.entryNumber-1
        if self.entryNumber<1:
            self.entryNumber=1
        self.tupleResult=self.db.goToEntry(self.entryNumber, self.userID)

        self.entryNumber=self.tupleResult[1]
        self.idText.configure(text=str(self.entryNumber))
        self.plainTextField.delete("1.0","end")
        self.plainTextField.insert("end", self.tupleResult[3])
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0","end")
        self.cipherTextField.insert("end", self.tupleResult[4])
        self.cipherTextField["state"]="disabled"
        if self.tupleResult[5]=="caesar":
            self.firstEncryptionOptionValue.set("Caesar Cipher")
        elif self.tupleResult[5]=="hex":
            self.firstEncryptionOptionValue.set("Hex")
        elif self.tupleResult[5]=="base":
            self.firstEncryptionOptionValue.set("Base32")
        elif self.tupleResult[5]=="book":
            self.fileName=self.tupleResult[6]
            self.firstEncryptionOptionValue.set("Book Cipher")
        self.postNavigationEncryptionSetUp()

    def forward1CryptoGUI(self):
        maxNum=self.db.findMaxLength(self.userID)
        self.entryNumber=self.entryNumber+1
        if self.entryNumber>maxNum:
            self.entryNumber=maxNum
        self.tupleResult=self.db.goToEntry(self.entryNumber, self.userID)

        self.entryNumber=self.tupleResult[1]
        self.idText.configure(text=str(self.entryNumber))
        self.plainTextField.delete("1.0","end")
        self.plainTextField.insert("end", self.tupleResult[3])
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0","end")
        self.cipherTextField.insert("end", self.tupleResult[4])
        self.cipherTextField["state"]="disabled"
        if self.tupleResult[5]=="caesar":
            self.firstEncryptionOptionValue.set("Caesar Cipher")
        elif self.tupleResult[5]=="hex":
            self.firstEncryptionOptionValue.set("Hex")
        elif self.tupleResult[5]=="base":
            self.firstEncryptionOptionValue.set("Base32")
        elif self.tupleResult[5]=="book":
            self.fileName=self.tupleResult[6]
            self.firstEncryptionOptionValue.set("Book Cipher")
        self.postNavigationEncryptionSetUp()

    def forward2CryptoGUI(self):
        maxNum=self.db.findMaxLength(self.userID)
        self.entryNumber=self.entryNumber+2
        if self.entryNumber>maxNum:
            self.entryNumber=maxNum
        self.tupleResult=self.db.goToEntry(self.entryNumber, self.userID)

        self.entryNumber=self.tupleResult[1]
        self.idText.configure(text=str(self.entryNumber))
        self.plainTextField.delete("1.0","end")
        self.plainTextField.insert("end", self.tupleResult[3])
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0","end")
        self.cipherTextField.insert("end", self.tupleResult[4])
        self.cipherTextField["state"]="disabled"
        if self.tupleResult[5]=="caesar":
            self.firstEncryptionOptionValue.set("Caesar Cipher")
        elif self.tupleResult[5]=="hex":
            self.firstEncryptionOptionValue.set("Hex")
        elif self.tupleResult[5]=="base":
            self.firstEncryptionOptionValue.set("Base32")
        elif self.tupleResult[5]=="book":
            self.fileName=self.tupleResult[6]
            self.firstEncryptionOptionValue.set("Book Cipher")
        self.postNavigationEncryptionSetUp()

    def forwardAllCryptoGUI(self):
        maxLength=self.db.findMaxLength(self.userID)
        self.tupleResult=self.db.goToEntry(maxLength, self.userID)

        self.entryNumber=self.tupleResult[1]
        self.idText.configure(text=str(self.entryNumber))
        self.plainTextField.delete("1.0","end")
        self.plainTextField.insert("end", self.tupleResult[3])
        self.cipherTextField["state"]="normal"
        self.cipherTextField.delete("1.0","end")
        self.cipherTextField.insert("end", self.tupleResult[4])
        self.cipherTextField["state"]="disabled"
        if self.tupleResult[5]=="caesar":
            self.firstEncryptionOptionValue.set("Caesar Cipher")
        elif self.tupleResult[5]=="hex":
            self.firstEncryptionOptionValue.set("Hex")
        elif self.tupleResult[5]=="base":
            self.firstEncryptionOptionValue.set("Base32")
        elif self.tupleResult[5]=="book":
            self.firstEncryptionOptionValue.set("Book Cipher")
        self.postNavigationEncryptionSetUp()
        