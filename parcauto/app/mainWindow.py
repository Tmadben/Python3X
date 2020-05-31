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
cursorLocal = conn.cursor(buffered=True)



## The main Screen: Ecran Principal contenant le menu
master = Tk()

#Global Variables : variables globales utilisées pour les champs, liste déroulantes et cases à cocher
varNumTicket = StringVar()
varSearchTicket = StringVar()
varMatricule = StringVar()
varDatArr = StringVar()
varDatDep = StringVar()
varTarifId = IntVar()
varTarifName = StringVar()
varTarif = StringVar()
varTarifPrice = IntVar()
varTarifTab = []


############################################
# # # DATA PROCESSING FUNCTIONS SPACE # # #
#  ESPACE DEDIE AU TRAITEMENT DES DONNEES #
############################################

# Function: Retrieve the list of all the enregistrements
def findAllEnregistrements(myTreeView):

    dataRow = []
    dataRow.clear()
    # Opérations à réaliser sur la base ...
    cursorLocal.execute("""SELECT id, num_vehicule, num_ticket, nom_tarif, time_arri, time_depa, duree, prix_tarif, montant FROM tbl_enregistrements;""")
    resultCol = cursorLocal.fetchall()

    for row in resultCol:
        dataRow.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]])
    
    for (dd,veh,tic,nmt,tma,tmd,dur,pta,mtn) in dataRow:
        myTreeView.insert("","end", values=(dd,veh,tic,nmt,tma,tmd,dur,pta,mtn))
#End of retrieve function


def getTarifTab():
    varTarifTab.clear()
    cursorLocal.execute("SELECT * FROM tbl_tarifs")
    record = cursorLocal.fetchall()
    for row in record:
        varTarifTab.append([row[1],row[2]])   
    

def newTicket():
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
    varDatArr.set(now.strftime('%Y-%m-%d %H:%M:%S'))

def initTicket():

    varNumTicket.set('')
    varDatArr.set('')
    varMatricule.set('')
    varTarifId.set('')



def saveEnregistrement():

    varTarifName.set(varTarif.get().split()[0])
    varTarifPrice.set(varTarif.get().split()[1])
    if varNumTicket.get() != '' and varMatricule.get() != '' and varDatArr.get() !='' and varTarifName.get() != '' and varTarifPrice.get() !='':
        reference = {'numTicket': varNumTicket.get(), 'matricule': varMatricule.get(), 'timeArr' : varDatArr.get(), 'nomTarif' : varTarifName.get(), 'prixTarif' : varTarifPrice.get()}
        cursorLocal.execute("""INSERT INTO tbl_enregistrements (num_ticket, num_vehicule, time_arri, nom_tarif, prix_tarif) VALUES(%(numTicket)s, %(matricule)s, %(timeArr)s, %(nomTarif)s, %(prixTarif)s)""", reference)
        conn.commit()
        # Show Message after saving
        messagebox.showinfo("Enregistrement","Véhicule: N°" + varMatricule.get() + " Ticket N°" + varNumTicket.get() + " enregistré avec succès!" )
        #Initialise all the fields
        initTicket()
    else:
        messagebox.showinfo("Enregistrement","Enregistrement impossible, champs vides!" )
# End function Save


#################################
# # # FORMS CREATION SPACCE # # #
# # ESPACE POUR LES FENETRES # #
#################################

# Function: Retrieve the details of the selected row
def getSelectedRow(myTreeView):
    messagebox

def enregistrementsFormShow():
    enregistrementsForm = tk.Toplevel(master)
    
    # Add PanelWindow
    pan = PanedWindow(enregistrementsForm, orient=HORIZONTAL)
    pan.grid(row=1, column=0)

    # Add all the Labels
    lbNumTicket = Label(enregistrementsForm, text = "N° Ticket : ")
    #lbNumTicket.grid(row = 2, column = 0, sticky = W, pady = 2)
    pan.add(lbNumTicket)

    # Add all the entry
    enNumTicket = Entry(enregistrementsForm, textvariable=varSearchTicket, width=22)
    #enNumTicket.grid(row = 2, column = 0, sticky = W, pady = 2, padx = 10)
    pan.add(enNumTicket)

    # Add Button save
    btSave = ttk.Button(enregistrementsForm, text="Rechercher", command='')
    btSave.config(width = 10)
    #btSave.grid(row = 2, column = 0, sticky = W, pady = 2, padx = 10)
    pan.add(btSave)

     # Headings list creation : Liste pour les entêtes
    cols = ("N°","MATRICULE","N°TICKET","TYPE TARIF","ARRIVEE","DEPART","DUREE", "PRIX UNIT","MONTANT")
    # TreeView Creation: Creation du tableau de listing
    tbl = ttk.Treeview(enregistrementsForm, columns=cols, show='headings', selectmode="browse")

    # set column headings: Ajout des entêtes au tableau
    for col in cols:
        tbl.heading(col, text=col, anchor="center")    

    
    #Fill the Tree View with function findAllStudents() : Remplissage du tableau avec la fonction findAllStudents
    findAllEnregistrements(tbl)

    tbl.bind("<ButtonRelease-1>", lambda event, t=tbl: getSelectedRow(t))

    tbl.column("N°", minwidth=0, width=40)
    tbl.column("MATRICULE", minwidth=0, width=120)
    tbl.column("N°TICKET", minwidth=0, width=160)
    tbl.column("TYPE TARIF", minwidth=0, width=110)
    tbl.column("ARRIVEE", minwidth=0, width=165)
    tbl.column("DEPART", minwidth=0, width=165)
    tbl.column("DUREE", minwidth=0, width=60)
    tbl.column("PRIX UNIT", minwidth=0, width=90)
    tbl.column("MONTANT", minwidth=0, width=120)
    tbl.grid(row=2, column=0,  padx=5, pady=5)
    

    enregistrementsForm.title("LISTE - ENREGISTREMENTS")
    enregistrementsForm.geometry("1050x400")
    enregistrementsForm.resizable(0, 0) 
    enregistrementsForm.grab_set()


def generateTicketFormShow():
    ticketForm = tk.Toplevel(master)
    
    #Init tarifs tab
    getTarifTab()
    
    # Add all the Labels
    lbNumTicket = Label(ticketForm, text = "N° Ticket : ")
    lbNumTicket.grid(row = 1, column = 0, sticky = W, pady = 2)
    lbDateArrivee = Label(ticketForm, text = "Date Arrivée : ")
    lbDateArrivee.grid(row = 2, column = 0, sticky = W, pady = 2)
    lbTarif = Label(ticketForm, text = "Tarif associé : ")
    lbTarif.grid(row = 3, column = 0, sticky = W, pady = 2)
    lbMatricule = Label(ticketForm, text = "N° Matricule : ")
    lbMatricule.grid(row = 4, column = 0, sticky = W, pady = 2)

    # Add all the entry
    enNumTicket = Entry(ticketForm, textvariable=varNumTicket, width=22)
    enNumTicket.grid(row = 1, column = 1, sticky = W, pady = 2, padx = 10)
    enDateArrivee = Entry(ticketForm, textvariable=varDatArr, width=22)
    enDateArrivee.grid(row = 2, column = 1, sticky = W, pady = 2, padx = 10)
    cbTarif = ttk.Combobox(ticketForm, values=varTarifTab, width=10, textvariable=varTarif)
    cbTarif.config(width=19)
    cbTarif.grid(row = 3, column=1, sticky = W, pady = 2, padx = 10)
    enNumMatricule = Entry(ticketForm, textvariable=varMatricule, width=22)
    enNumMatricule.grid(row = 4, column = 1, sticky = W, pady = 2, padx = 10)
    
    # Add Button save
    btSave = ttk.Button(ticketForm, text="Enregistrer", command=saveEnregistrement )
    btSave.config(width = 35)
    btSave.grid(row = 5, column = 0, columnspan=3, sticky = W, pady = 2, padx = 10)

    ticketForm.title("TDKT - TICKET")
    ticketForm.geometry("260x150")
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
btListenregistrement = Button(master, text = "Enregistrements", height=1, width=25, command=enregistrementsFormShow)
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
master.title("GESTION PARKING TDKT Comp  -  MENU PRINCIPAL")
master.geometry("730x400")
master.resizable(0, 0) 
mainloop() 
