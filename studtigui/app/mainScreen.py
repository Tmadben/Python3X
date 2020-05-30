# import tkinter module 
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

## DB Connexion string : Chaine d accès à la base de données
conn = mysql.connector.connect(host="127.0.0.1",
user="root", password="root",
database="bd_student")



## The main Screen: Ecran Principal contenant le menu
master = Tk()

#Global Variables : variables globales utilisées pour les champs, liste déroulantes et cases à cocher
varFirstName = StringVar()
varLastName = StringVar()
varAge = IntVar()
varSexe = StringVar()
varClasse = StringVar()
varNationality = StringVar()
varPhone = StringVar()
varEmail = StringVar()
varRows = []


#################################
# # # FORMS CREATION SPACCE # # #
# # ESPACE POUR LES FENETRES # #
#################################

## Save student Form: ENREGISTREMENT D'UN ETUDIANT
def saveFormShow():
    saveForm = tk.Toplevel(master)

    # Add all the Labels
    lbLastName = Label(saveForm, text = "NOM : ")
    lbLastName.grid(row = 1, column = 0, sticky = W, pady = 2)
    lbFirstName = Label(saveForm, text = "PRENOM(S) : ")
    lbFirstName.grid(row = 2, column = 0, sticky = W, pady = 2)
    lbAge = Label(saveForm, text = "AGE : ")
    lbAge.grid(row = 3, column = 0, sticky = W, pady = 2)
    lbSexe = Label(saveForm, text = "SEXE : ")
    lbSexe.grid(row = 4, column = 0, sticky = W, pady = 2)
    lbNationality = Label(saveForm, text = "NATIONALITE : ")
    lbNationality.grid(row = 5, column = 0, sticky = W, pady = 2)
    lbClasse = Label(saveForm, text = "CLASSE : ")
    lbClasse.grid(row = 6, column = 0, sticky = W, pady = 2)

    # Add all the entry
    enLastName = Entry(saveForm, textvariable=varLastName, width=40)
    enLastName.grid(row = 1, column = 1, columnspan=2, sticky = W, pady = 2)
    enFirstName = Entry(saveForm, textvariable=varFirstName, width=40)
    enFirstName.grid(row = 2, column = 1, columnspan=2, sticky = W, pady = 2)
    enAge = Entry(saveForm, textvariable=varAge, width=10)
    enAge.grid(row = 3, column = 1, columnspan=2, sticky = W, pady = 2)
    rbSexeM = Radiobutton(saveForm, text="M", variable=varSexe, value="Masculin")
    rbSexeM.grid(row = 4, column = 1, sticky = W, pady = 2)
    rbSexeF = Radiobutton(saveForm, text="F", variable=varSexe, value="Feminin")
    rbSexeF.grid(row = 4, column = 2, sticky = W, pady = 2)
    cbNationality = ttk.Combobox(saveForm, values=["France","Cote D'Ivoire","Mali","Burkina Faso", "USA", "Canada"], width=37, textvariable=varNationality)
    cbNationality.grid(row = 5, column=1, columnspan=2, sticky = W, pady = 2)
    cbClasse = ttk.Combobox(saveForm, values=["IT RESEAUX","IC RESEAUX","IT GENIE LOGICIEL","IC GENIE LOGICIEL", "IT FINANCE", "IC FINANCE"], width=37, textvariable=varClasse)
    cbClasse.grid(row = 6, column=1, columnspan=2, sticky = W, pady = 2)
    
    # Add Buttons Valider and Annuler
    btAnnuler = ttk.Button(saveForm, text="Annuler", command = initSaveStudent)
    btAnnuler.grid(row = 8, column = 1, sticky = W, pady = 2)
    btSave = ttk.Button(saveForm, text="Valider", command = saveStudent )
    btSave.grid(row = 8, column = 2, sticky = W, pady = 2)

    
    saveForm.title("ENREGISTRER UN ETUDIANT")
    saveForm.grab_set() #Set a form as modal
## End of SaveForm function
    


# Students LISTING Form
def listStudentFormShow():

    listStudentForm = tk.Toplevel(master)

    # Headings list creation : Liste pour les entêtes
    cols = ("MATRICULE","NOM","PRENOM(S)","SEXE","AGE","PAYS","CLASSE")
    # TreeView Creation: Creation du tableau de listing
    tblStudents = ttk.Treeview(listStudentForm, columns=cols, show='headings', selectmode="browse")

    # set column headings: Ajout des entêtes au tableau
    for col in cols:
        tblStudents.heading(col, text=col, anchor="center")    

    #Form Title : Titre de la fenêtre de listing
    lbTitreList = Label(listStudentForm, text = "LISTING DES ETUDIANTS INSCRITS : ")
    lbTitreList.grid(row = 0, column = 0, sticky = W+E, pady = 2)
    
    #Fill the Tree View with function findAllStudents() : Remplissage du tableau avec la fonction findAllStudents
    findAllStudents(tblStudents)
    tblStudents.bind("<ButtonRelease-1>", lambda event, t=tblStudents: getSelectedRow(t))

    tblStudents.grid(row=1, column=0)
    listStudentForm.title("LISTE DES ETUDIANTS")
    listStudentForm.grab_set()
#End of LISTING

# Form for Editing a student : Fenetre de modification 
def editStudentFormShow():
    editStudentForm = tk.Toplevel(master)
    editStudentForm.title("MODIFIER LES INFOS D'UN ETUDIANT")
    editStudentForm.grab_set()
#End of Editing form

#Form for deleting a student : Fenetre de suppression
def deleteStudentFormShow():
    deleteStudentForm = tk.Toplevel(master)
    deleteStudentForm.title("SUPPRIMER UN ETUDIANT")
    deleteStudentForm.grab_set()
#End of deleting form


############################################
# # # DATA PROCESSING FUNCTIONS SPACE # # #
#  ESPACE DEDIE AU TRAITEMENT DES DONNEES #
############################################  

# Save a Student function
def saveStudent():

    cursorLocal = conn.cursor()
    reference = {'firstname': varFirstName.get(), 'lastname' : varLastName.get(), 'age' : varAge.get(), 'sexe' : varSexe.get(), 'nationality' : varNationality.get(), 'classe' : varClasse.get()}
    cursorLocal.execute("""INSERT INTO students (firstname, lastname, age, sexe, nationality, classe) VALUES(%(firstname)s, %(lastname)s, %(age)s, %(sexe)s, %(nationality)s, %(classe)s)""", reference)
    cursorLocal.close()

    # Show Message after saving
    messagebox.showinfo("Enregistrement","Etudiant: " + varFirstName.get() + " " + varLastName.get() + " enregistré avec succès!" )
    
    #Initialise all the fields
    varFirstName.set("")
    varLastName.set("")
    varAge.set(0)
    varNationality.set("")
    varClasse.set("")
# End function Save student


# Initialise student saving form
def initSaveStudent():

    #Initialise all the fields
    varFirstName.set("")
    varLastName.set("")
    varAge.set(0)
    varNationality.set("")
    varClasse.set("")
# End of init


# Function: Retrieve the list of all the students
def findAllStudents(myTreeView):

    dataRow = []
    cursorLocal = conn.cursor()
    # Opérations à réaliser sur la base ...
    cursorLocal.execute("""SELECT matricule, lastname, firstname, sexe, age, nationality, classe FROM students;""")
    resultCol = cursorLocal.fetchall()

    for row in resultCol:
        dataRow.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
    
    for (mat,lsn,fsn,sex,age,nat,cla) in dataRow:
        myTreeView.insert("","end", values=(mat,lsn,fsn,sex,age,nat,cla))
        
    
    cursorLocal.close()
#End of retrieve function

# Function: Retrieve the details of the selected row
def getSelectedRow(myTreeView):
    selectedRow = myTreeView.item(myTreeView.focus())["values"]
    print (selectedRow)




#############################
# # # MAIN SCREEN SPACE # # #
# # #  MENU PRINCIPAL   # # #
#############################
  

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