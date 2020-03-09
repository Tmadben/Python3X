# import tkinter module 
from tkinter import * 
import tkinter as tk

master = Tk()


def enregistrerShow():
    enregistrer = tk.Toplevel(master)
    enregistrer.title("ENREGISTREMENT ETUDIANT")    


  
# button widget main menu
b1 = Button(master, text = "Enregistrer", height=1, width=25, command=enregistrerShow)
b1.pack()
b2 = Button(master, text = "Afficher", height=1, width=25)
b2.pack()
b3 = Button(master, text = "Modifier", height=1, width=25)
b3.pack()
b4 = Button(master, text = "Supprimer",height=1, width=25,)
b4.pack()
b5 = Button(master, text = "Quitter", height=1, width=25, command=master.quit)
b5.pack()


master.title("MENU PRINCIPAL")
master.mainloop() 