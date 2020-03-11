# import tkinter module 
from tkinter import * 
import tkinter as tk


## The main Screen
master = Tk()

## All the form for saving, listing, editing, deleting students
def saveFormShow():
    saveForm = tk.Toplevel(master)
    saveForm.title("ENREGISTRER UN ETUDIANT")
    saveForm.grab_set() #Set a form as modal

def listStudentFormShow():
    listStudentForm = tk.Toplevel(master)
    listStudentForm.title("LISTE DES ETUDIANTS")
    listStudentForm.grab_set()

def editStudentFormShow():
    editStudentForm = tk.Toplevel(master)
    editStudentForm.title("MODIFIER LES INFOS D'UN ETUDIANT")
    editStudentForm.grab_set()

def deleteStudentFormShow():
    deleteStudentForm = tk.Toplevel(master)
    deleteStudentForm.title("SUPPRIMER UN ETUDIANT")
    deleteStudentForm.grab_set()


  
# button widget main menu
## Save a student form
btOpenSaveForm = Button(master, text = "Enregistrer", height=1, width=25, command=saveFormShow)
btOpenSaveForm.pack()

## List all the students form
btOpenListForm = Button(master, text = "Afficher", height=1, width=25, command=listStudentFormShow)
btOpenListForm.pack()

## Edit a student form
btEditStudentForm = Button(master, text = "Modifier", height=1, width=25, command=editStudentFormShow)
btEditStudentForm.pack()

## Delete a student form
btDeleteStudentForm = Button(master, text = "Supprimer",height=1, width=25, command=deleteStudentFormShow)
btDeleteStudentForm.pack()

## Shut down the app
btQuit = Button(master, text = "Quitter", height=1, width=25, command=master.quit)
btQuit.pack()


##Open The main Screen 
master.title("MENU PRINCIPAL")
master.mainloop() 