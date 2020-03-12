# import tkinter module 
from tkinter import * 
import tkinter as tk
from tkinter import ttk


## The main Screen
master = Tk()

#Global Variables
varFirstName = StringVar()
varLastName = StringVar()
varAge = int()
varSexe = StringVar()
varClasse = StringVar()
varNationality = StringVar()
varPhone = StringVar()
varEmail = StringVar()


## Save student Form: ENREGISTREMENT D'UN ETUDIANT
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

    # Add all the entry
    enFirstName = Entry(saveForm, textvariable=varFirstName, width=40)
    enFirstName.grid(row = 1, column = 1, columnspan=2, sticky = W, pady = 2)
    enLastName = Entry(saveForm, textvariable=varLastName, width=40)
    enLastName.grid(row = 2, column = 1, columnspan=2, sticky = W, pady = 2)
    enAge = Entry(saveForm, textvariable=varAge, width=10)
    enAge.grid(row = 3, column = 1, columnspan=2, sticky = W, pady = 2)
    rbSexeM = Radiobutton(saveForm, text="M", variable=varSexe, value="Masculin")
    rbSexeM.grid(row = 4, column = 1, sticky = W, pady = 2)
    rbSexeF = Radiobutton(saveForm, text="F", variable=varSexe, value="Feminin")
    rbSexeF.grid(row = 4, column = 2, sticky = W, pady = 2)
    cbNationality = ttk.Combobox(saveForm, values=["France","Cote D'Ivoire","Mali","Burkina Faso", "USA", "Canada"], width=37)
    cbNationality.grid(row = 5, column=1, columnspan=2, sticky = W, pady = 2)
    cbClasse = ttk.Combobox(saveForm, values=["IT RESEAUX","IC RESEAUX","IT GENIE LOGICIEL","IC GENIE LOGICIEL", "IT FINANCE", "IC FINANCE"], width=37)
    cbClasse.grid(row = 6, column=1, columnspan=2, sticky = W, pady = 2)
    
    # Add Buttons Save and erase
    btAnnuler = ttk.Button(saveForm, text="Annuler", command="")
    btAnnuler.grid(row = 8, column = 1, sticky = W, pady = 2)
    btSave = ttk.Button(saveForm, text="Valider", command="")
    btSave.grid(row = 8, column = 2, sticky = W, pady = 2)

    saveForm.title("ENREGISTRER UN ETUDIANT")
    saveForm.grab_set() #Set a form as modal
## End of SaveForm function



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