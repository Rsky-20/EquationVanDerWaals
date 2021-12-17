#!/bin/python3
# -*- coding: utf-8 -*- 
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox

Bienvenue = """                                                                                                                                                                                    
                                                                                            
Welcome on our App ! 
This app is a simulation Application about the famous equation of Van Der Waals
"""

Apropos = """
Version: 0.06
Commit: 8d7f385543319f9c1e60a2af9793a535ea9f245f
Date: 20/12/2021
@uthor: Pierre VAUDRY ; Enora GUILLAUME ; Safa HERELLI ; Jessy JOSE
Python: 3.10

"""

Help = """



"""

def BienvenuePage(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """
    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title(r"Welcome on ThermoSim App")
    
    text = tk.Text(app)
    text.tag_config("Debut", font=('Tahoma', 20))
    text.tag_config("Titre", font=('Tahoma', 20, 'bold', 'underline'), tabs=('3c', '5c', '12c'))
    text.tag_config("Paragraphe", font=('Tahoma', 10))
    
    text.insert(tk.END, 'Welcome Page', 'Titre')
    text.insert(tk.END, Bienvenue, 'Paragraphe')
    
    text.configure(state='disabled')
    text.place(relx=0, rely=0, relheight=1, relwidth=1)
    

def HelpPage(master):
    """
    [Description]

    :param master: master se réfaire à la page parent
    :return:
    """
    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)  # Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title(r"ThermoSim Help Page")
    
    text = tk.Text(app)
    text.tag_config("Debut", font=('Tahoma', 20))
    text.tag_config("Titre", font=('Tahoma', 20, 'bold', 'underline'), tabs=('3c', '5c', '12c'))
    text.tag_config("Paragraphe", font=('Tahoma', 10))
    
    text.insert(tk.END, 'Help Page', 'Titre')
    text.insert(tk.END, Help, 'Paragraphe')
    
    text.configure(state='disabled')
    text.place(relx=0, rely=0, relheight=1, relwidth=1)
    