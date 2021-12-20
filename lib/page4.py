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


def VanDerWaals(master):
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
    app.title("Représentation de l'equation mathématique de Van der Waals")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()
    
    x = np.arange(-20, 20.1, 0.0001)
    T = np.arange(0.5, 3.6, 0.5)
    
    
    def VDW(V, T):
        """[summary]

        Args:
            V ([type]): [description]
            T ([type]): [description]

        Returns:
            [type]: [description]
        """        
        a = 1
        b = 4
        R = 8.314472
        return T * R / (V - b) - a / (V**2)
    
    for i in range(0,len(T)):
        L="T"+str(i+1)+"("+str(T[i])+"K)"
        ax.plot(x,VDW(x,T[i]),label=L)
        
    # Graphe parts
    ax.axvline(x=0,color='black')
    ax.axvline(x=4,color='black',linewidth=0.3)
    ax.axhline(y=0,color='black')
    ax.axis([-15,15,-15,15])
    ax.set_ylabel(r"$P\;(Pa)$")
    ax.set_xlabel(r"$V_m\;(m^3.mol^{-1})$")
    ax.set_title("Représentation de l'equation mathématique de Van der Waals")
    ax.legend(loc='upper left')
    ax.axhspan(-15,0,color='orange',alpha=0.3)
    ax.axvspan(-15,4,color='orange',alpha=0.3)
    ax.text(7.8,12,u'Domaine')
    ax.text(7.8,10.8,u'physique')
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

