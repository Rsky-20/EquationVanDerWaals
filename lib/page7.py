#!/bin/python3
# -*- coding: utf-8 -*- 
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np


def Amagat(master):
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
    app.title("Coordonnées d'Amagat : PV en fonction de P")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()

    V = np.arange(0.05*pow(10, -3), 0.1,pow(10, -6))
    T = np.arange(300, 1301, 200)
    def VDWCO_2(V, T):
        """[summary]

        Args:
            V ([type]): [description]
            T ([type]): [description]

        Returns:
            [type]: [description]
        """        
        R = (8.314472)
        a = 363.7*pow(10, -3)
        b = 0.0427*pow(10, -3)
        return T * R / (V - b) - a / (V**2)
    
    
    def GP(V, T):
        """[summary]

        Args:
            V ([type]): [description]
            T ([type]): [description]

        Returns:
            [type]: [description]
        """        
        R = (8.314472)
        return T * R / V
    
    
    def GPAmagat(V, T):
        """[summary]

        Args:
            V ([type]): [description]
            T ([type]): [description]

        Returns:
            [type]: [description]
        """        
        R = 8.314472
        return (GP(V, T) * V)
    
    
    def VDWCO_2Amagat(V, T):
        """[summary]

        Args:
            V ([type]): [description]
            T ([type]): [description]

        Returns:
            [type]: [description]
        """        
        return VDWCO_2(V, T) * V
    
    
    for i in range(0, len(T)):
        lab = "T" + str(i+1) + "(" + str(T[i]) + "K) VDW"
        ax.plot(VDWCO_2(V, T[i]), VDWCO_2Amagat(V, T[i]), color='b', label=lab)
    for i in range(0, len(T)):
        lab="T" + str(i+1) + "(" + str(T[i]) + "K) GP"
        ax.plot(GP(V, T[i]), GPAmagat(V,T[i]), color='r', label=lab)
    ax.axis([0, 2.5*pow(10, 7), 0,9*pow(10, 3)])
    ax.set_ylabel(r'$PV\;(Pa.m^3)$')
    ax.set_xlabel(r'$P\;(Pa)$')
    ax.set_title("Coordonnées d'Amagat : PV en fonction de P")
    ax.grid(b=True, which='major', color='#666666', linestyle='-')
    

    canvas = FigureCanvasTkAgg(fig, master=app)  # A tk.DrawingArea.
    canvas.draw()

    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, app, pack_toolbar=False)
    toolbar.update()

    canvas.mpl_connect(
        "key_press_event", lambda event: print(f"you pressed {event.key}"))
    canvas.mpl_connect("key_press_event", key_press_handler)

    toolbar.pack(side=tk.TOP, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

