# import tkinter module 
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

## DB Connexion string : Chaine d accès à la base de données
conn = mysql.connector.connect(host="127.0.0.1",
user="root", password="root",
database="parcauto_db")



## The main Screen: Ecran Principal contenant le menu
master = Tk()



#############################
# # # MAIN SCREEN SPACE # # #
# # #  MENU PRINCIPAL   # # #
#############################
  

# button widget main menu
## To generate new ticket
btOpenSaveForm = Button(master, text = "Générer ticket", height=1, width=25, command='')
btOpenSaveForm.grid(row = 1, column = 0)

## To edit the existing tarifs
btOpenListForm = Button(master, text = "Tarifs associés", height=1, width=25, command='')
btOpenListForm.grid(row = 1, column = 1)

## Shut down the app
btQuit = Button(master, text = "Quitter", height=1, width=25, command=master.quit)
btQuit.grid(row = 1, column = 2)


##Open The main Screen 
master.title("GESTION PARCKING TDKT -  MENU PRINCIPAL")
master.geometry("550x400")
master.resizable(0, 0) 
mainloop() 