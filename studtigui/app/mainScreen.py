# import tkinter module 
from tkinter import * 
import tkinter as tk


## The main Screen
master = Tk()

#Gloabl Variables
varFirstName = StringVar()
varLastName = StringVar()
varAge = int()
varSexe = StringVar()
varClasse = StringVar()
varNationality = StringVar()
varPhone = StringVar()
varEmail = StringVar()


## All the form for saving, listing, editing, deleting students
def saveFormShow():
    saveForm = tk.Toplevel(master)

    # Add all the Labels
    lbFirstName = Label(saveForm, text = "NOM : ")
    lbFirstName.grid(row = 1, column = 0, sticky = W, pady = 2)
    lbLastName = Label(saveForm, text = "PRENOM(S) : ")
    lbLastName.grid(row = 2, column = 0, sticky = W, pady = 2)
    lbAge = Label(saveForm, text = "AGE : ")
    lbAge.grid(row = 3, column = 0, sticky = W, pady = 2)
    lbSexe = Label(saveForm, text = "SEXE : ")
    lbSexe.grid(row = 4, column = 0, sticky = W, pady = 2)
    lbNationality = Label(saveForm, text = "NATIONALITE : ")
    lbNationality.grid(row = 5, column = 0, sticky = W, pady = 2)
    lbClasse = Label(saveForm, text = "CLASSE : ")
    lbClasse.grid(row = 6, column = 0, sticky = W, pady = 2)

    # Add entry
    enFirstName = Entry(saveForm, textvariable=varFirstName)
    enFirstName.grid(row = 1, column = 1, sticky = W, pady = 2)
    enLastName = Entry(saveForm, textvariable=varLastName)
    enLastName.grid(row = 2, column = 1, sticky = W, pady = 2)
    enAge = Entry(saveForm, textvariable=varAge)
    enAge.grid(row = 3, column = 1, sticky = W, pady = 2)
    

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
btOpenSaveForm.grid(row = 1, column = 0)

## List all the students form
btOpenListForm = Button(master, text = "Afficher", height=1, width=25, command=listStudentFormShow)
btOpenListForm.grid(row = 2, column = 0)

## Edit a student form
btEditStudentForm = Button(master, text = "Modifier", height=1, width=25, command=editStudentFormShow)
btEditStudentForm.grid(row = 3, column = 0)

## Delete a student form
btDeleteStudentForm = Button(master, text = "Supprimer",height=1, width=25, command=deleteStudentFormShow)
btDeleteStudentForm.grid(row = 4, column = 0)

## Shut down the app
btQuit = Button(master, text = "Quitter", height=1, width=25, command=master.quit)
btQuit.grid(row = 5, column = 0)


##Open The main Screen 
master.title("MENU PRINCIPAL")
mainloop() 