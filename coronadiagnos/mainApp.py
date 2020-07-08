# CoronaDiagnos is a terminal application for COVID-19 screening
#  

# Welcome into the CoronaDiagnos App

import sys
import datetime
import time
import os
import keyboard


#Declaration & instanciation des variables à utiliser
varCivilite = "Mme/Mle/Mr"
varNom = ""
varPrenom = ""
varAge = ""
now = datetime.datetime.now()

def headerTitle():
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
    


def introAnalya():
    time.sleep(6)
    print("\tJe suis Analya, une Intelligence Artificielle,")
    time.sleep(4)
    print("\tqui vous assistera pour votre diagnostique.")
    print("\n")
    time.sleep(4)
    print("\tMaintenant que vous savez qui je suis, hahaha,")
    time.sleep(5)
    print("\tje vais vous aider à vous présenter, Ok?")
    print("\n")
    time.sleep(3)
    print("\tAllez, on y va!")
    print("\n")


def salutation():
    time.sleep(5)
    if(int(now.hour) > 10):
        print("\tBonsoir " + varCivilite)
    else:
        print("\tBonjour " + varCivilite)
    print("\n")


def startAnalya():
    os.system('cls')
    headerTitle()
    introAnalya()
    salutation()
    

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