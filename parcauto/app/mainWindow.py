# import tkinter module 
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import *
import mysql.connector

## DB Connexion string : Chaine d accès à la base de données
conn = mysql.connector.connect(host="127.0.0.1",
user="root", password="root",
database="parcauto_db")



## The main Screen: Ecran Principal contenant le menu
master = Tk()

#Global Variables : variables globales utilisées pour les champs, liste déroulantes et cases à cocher
varNumTicket = StringVar()
varDatArr = StringVar()
varDatDep = StringVar()
varTarifId = IntVar()
varTarifName = StringVar()
varTarifPrice = IntVar()


############################################
# # # DATA PROCESSING FUNCTIONS SPACE # # #
#  ESPACE DEDIE AU TRAITEMENT DES DONNEES #
############################################ 
def newTicket():
    cursorLocal = conn.cursor()
    cursorLocal.execute("SELECT * FROM tbl_enregistrements")
    numberOfRow = cursorLocal.rowcount
    if numberOfRow < 0 :
        numberOfRow = 1
    else:
        numberOfRow = numberOfRow + 1

    now = datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    second = '{:02d}'.format(now.second)
    varNumTicket.set(year + '-' + month + '-TDKT' + '-' + '{:08d}'.format(numberOfRow))
    dateFormat = '{}-{}-{} {}:{}:{}'.format(year, month, day, hour, minute, second)
    varDatArr.set(dateFormat)
    cursorLocal.close



#################################
# # # FORMS CREATION SPACCE # # #
# # ESPACE POUR LES FENETRES # #
#################################

def generateTicketFormShow():
    ticketForm = tk.Toplevel(master)
    
    
     # Add all the Labels
    lbNumTicket = Label(ticketForm, text = "N° Ticket : ")
    lbNumTicket.grid(row = 1, column = 0, sticky = W, pady = 2)
    lbDateArrivee = Label(ticketForm, text = "Date Arrivée : ")
    lbDateArrivee.grid(row = 2, column = 0, sticky = W, pady = 2)
    lbTarif = Label(ticketForm, text = "Tarif associé : ")
    lbTarif.grid(row = 3, column = 0, sticky = W, pady = 2)

    # Add all the entry
    enNumTicket = Entry(ticketForm, textvariable=varNumTicket, width=22)
    enNumTicket.grid(row = 1, column = 1, sticky = W, pady = 2)
    enDateArrivee = Entry(ticketForm, textvariable=varDatArr, width=22)
    enDateArrivee.grid(row = 2, column = 1, sticky = W, pady = 2)
    cbTarifPrice = ttk.Combobox(ticketForm, values=[500,1000,1500], width=10, textvariable=varTarifPrice)
    cbTarifPrice.grid(row = 3, column=1, sticky = W, pady = 2)
    btSave = ttk.Button(ticketForm, text="Enregistrer", command = '' )
    btSave.config(width = 35)
    btSave.grid(row = 4, column = 0, columnspan=3, sticky = W, pady = 2)

    ticketForm.title("TICKET NUMERIQUE")
    ticketForm.geometry("280x150")
    ticketForm.resizable(0, 0) 
    ticketForm.grab_set()
    newTicket()




#############################
# # # MAIN SCREEN SPACE # # #
# # #  MENU PRINCIPAL   # # #
#############################
  

# button widget main menu
## To generate new ticket
btOpenSaveForm = Button(master, text = "Générer ticket", height=1, width=25, command=generateTicketFormShow)
btOpenSaveForm.grid(row = 1, column = 0)

## Shut down the app
btListenregistrement = Button(master, text = "Enregistrements", height=1, width=25, command='')
btListenregistrement.grid(row = 1, column = 1)

## To edit the existing tarifs
btOpenListForm = Button(master, text = "Tarifs associés", height=1, width=25, command='')
btOpenListForm.grid(row = 1, column = 3)

## Shut down the app
btQuit = Button(master, text = "Quitter", height=1, width=25, command=master.quit)
btQuit.grid(row = 1, column = 4)

path = "../image/tdkt_logo.png"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(master, image = img)
panel.grid(row = 4, column = 0, columnspan=5, sticky=W+E+N+S, padx=2, pady=2)



##Open The main Screen 
master.title("GESTION PARKING TDKT Comp-  MENU PRINCIPAL")
master.geometry("730x400")
master.resizable(0, 0) 
mainloop() 
