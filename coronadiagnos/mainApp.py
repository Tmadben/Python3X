### CoronaDiagnos is a terminal 
### application for COVID-19 screening
### Welcome into the CoronaDiagnos App


# Importation des bibliothèques
import sys
import datetime
import time
import os
import keyboard


#Declaration & instanciation des variables à utiliser
varCivilite = ""
varNumIdentifiant = ""
varAge = ""
now = datetime.datetime.now()

#Entete de l'application
def headerTitle():
    os.system('cls')
    print("\n")
    print("\t***********************************************")
    print("\t***********************************************")
    print("\t******-------------------------------------****")
    print("\t****  Bienvenue sur CoronaDiagnos App 1.0.0 ***")
    print("\t******-------------------------------------****")
    print("\t***********************************************")
    print("\t***********************************************")
    print ("\t| DATE : " + now.strftime("%Y-%m-%d") + " |")
    print("\t---------------------")
    print("\n")
    

# Analya se présente
def introAnalya():
    time.sleep(3)
    print("\tJe suis Analya, une Intelligence Artificielle,")
    time.sleep(3)
    print("\tqui vous assistera pour votre diagnostique.")
    print("\n")
    time.sleep(3)
    print("\tMaintenant que vous savez qui je suis, LOOLLLL")
    time.sleep(3)
    print("\tje vais vous aider à vous présenter, Ok?")
    print("\n")
    time.sleep(3)
    print("\tAllez, on y va!")
    time.sleep(2)
    print("\n")
    print("\n")


# Présentez-vous: Votre Identifiant
def infoAge():
    global varAge
    print("\tIndiquez votre Age et appuyez sur la touche ENTREE")
    ageValue = input("\tVotre Age : ").replace(" ","")
    if(ageValue.isnumeric ):
        varAge = int(ageValue)
        print("\tReponse : " + str(varAge) + " ans")
        print("\n")
    else:
        print("\tOh! Mais non, ce n'est pas un nombre ça!")
        time.sleep(2)
        print("\t... Allez on recommence")
        print("\n")
        time.sleep(4)
        headerTitle()
        infoAge()


# Présentez-vous: Votre Identifiant
def infoIdentitifiant():
    global varNumIdentifiant
    print("\tIndiquez votre N° et appuyez sur la touche ENTREE")
    varNumIdentifiant = input("\tVotre N° Indentifiant: ")
    if(varNumIdentifiant.replace(" ","") != ""):
        print("\tReponse : " + varNumIdentifiant)
        print("\n")
        infoAge()
    else:
        print("\tLe champs est vide, voyons... Allez on recommence")
        print("\n")
        time.sleep(4)
        headerTitle()
        infoIdentitifiant()


# Présentez-vous: Votre Civilité
def infoCivilite():
    global varCivilite
    headerTitle()
    time.sleep(4)
    print("\tAppuyez sur la touche qui vous correspond")
    print("\n")
    time.sleep(4)
    print("\tCivilité: ")
    print("\n")
    print("\t(a) : Mlle")
    print("\t(z) : Mme")
    print("\t(e) : Mr")
    print("\n")
    if keyboard.read_key() == "a":
        varCivilite = "Mlle"
        print("\tReponse: " + varCivilite)
        print("\n")
        infoIdentitifiant()
    elif keyboard.read_key() == "z":
        varCivilite = "Mme"
        print("\tReponse: " + varCivilite)
        print("\n")
        infoIdentitifiant()
    elif keyboard.read_key() == "e":
        varCivilite = "Mr"
        print("\tReponse: " + varCivilite)
        print("\n")
        infoIdentitifiant()
    else:
        time.sleep(4)
        print("\tOups! Votre choix semble ne pas exister")
        time.sleep(2)
        print("\n")
        print("\tNous allons réessayer, d'accord? C'est parti")
        time.sleep(3)
        infoCivilite()


# Analya vous salue
def salutation():
    print("\n")
    print("\n")
    time.sleep(5)
    if(int(now.hour) > 16):
        print("\tBonsoir " + varCivilite + " " + varNumIdentifiant)
    else:
        print("\tBonjour " + varCivilite + " " + varNumIdentifiant)
    time.sleep(2)
    print("\n")
    if (varAge < 21):
        print("\tVous n'êtes pas encore majeur, à ce que je vois!")
    elif (varAge < 40):
        print("\tVous êtes à l'entrée de l'age adulte, formidable ça!")
    elif (varAge < 50):
        print("\tAh oui, l'age de la maturité...")
    elif (varAge < 60):
        print("\tJ'ai un profond respect pour les cinquantenaires vous savez.")
    else:
        print("\tVous avez bien fait de venir vous faire diagnostiquer.")
    time.sleep(2)
    print("\n")



#Analya est mis en marche
def startAnalya():
    headerTitle()
    introAnalya()
    infoCivilite()
    salutation()
    
# Pour quitter Analya ou rester
def quitterAnalya():
    time.sleep(4)
    print("\n")
    print("\tAppuyez sur Q pour quitter ou une autre touche pour continuer: ")
    if keyboard.read_key() == "q":
        sys.exit()
    else:
       startAnalya()
       quitterAnalya()



## Starting Point
startAnalya()
quitterAnalya()