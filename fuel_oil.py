"""
Récupération du cours du fioul

Package installé : beautifulsoup4

Éditeur : Laurent REYNAUD
Date : 20/01/2021
"""

from tkinter import *
from bs4 import BeautifulSoup  # permet d'obtenir la mise à jour des données
import urllib  # récupération des données d'une URL
from urllib import request
from datetime import datetime  # mise à jour des données à un temps T
import locale  # conversion du module datetime en français

"""Configuration de la fenêtre principale"""
root = Tk()
root.title('Cours du jour !')
root.geometry('500x150')
root.config(bg='black')

"""Conversion des données du module time en français"""
locale.setlocale(locale.LC_TIME, 'FR')


def update_fueloil():
    """Mise à jour de cours du fioul"""

    """Récupération de la valeur du prix du fioul sur le site 'prix fioul'"""
    page = urllib.request.urlopen('https://prixfioul.fr/').read()  # accès au site internet
    html = BeautifulSoup(page, 'html.parser')  # récupération du code source
    unit_price = html.find(class_='superieur')  # récupération de la ligne où est affiché le prix du fioul supérieur
    unit_price1 = str(unit_price)  # conversion au format str
    unit_price2 = unit_price1[70:73]  # récupération de la valeur du fioul
    unit_price3 = round(float(unit_price2) / 1_000, 3)  # conversion aux prix du litre
    my_label_pricefueloil.config(text=f"{unit_price3} €")


"""Cadre pour le cours du fioul"""
my_frame = Frame(root, bg='black')
my_frame.pack(pady=20)

"""Création d'un titre fioul"""
my_label_fueloil = Label(my_frame, text='Cours du fioul :', fg='green', bg='black', font='Helvetica 20')
my_label_fueloil.grid(row=0, column=0, padx=10, pady=20)

"""Création du prix du fioul"""
my_label_pricefueloil = Label(my_frame, text='', fg='green', bg='black', font='Helvetica 20')
my_label_pricefueloil.grid(row=0, column=1, padx=10, pady=20)

"""Temps actuel"""
now = datetime.now()
current_date = now.strftime('%A %e %B %Y')
current_time = now.strftime('%H:%M:%S')

"""Barre de statut"""
status_bar = Label(root, text=f"Dernière mise à jour : le {current_date} à {current_time}     ",
                   anchor=E, bd=0, bg='black', fg='green')
status_bar.pack(side=BOTTOM, fill=X, ipady=10)

"""Appel de la fonction pour la mise à jour du cours du fioul"""
update_fueloil()

root.mainloop()
