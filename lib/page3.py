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


def GazParfait(master):
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
    app.title(r"Représentation mathématique de l'équation des gas parfaits")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()
    
    x = np.arange(-20,20.1,0.0001)
    T = np.arange(0.5,3.6,0.5)
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
    
    
    for i in range(0, len(T)):
        L = "T" + str(i+1) + "(K)"
        ax.plot(x, GP(x, T[i]), linewidth=1, label=L)
    ax.axvline(x=0, color='black')
    ax.axhline(y=0, color='black')
    ax.axis([-20, 20, -20, 20])
    ax.set_ylabel('P (Pa)')
    ax.set_xlabel(r"$V_m\; (m^3.mol^{-1})$")
    ax.set_title(r"Représentation mathématique de l'équation des gas parfaits")
    ax.text(7, 9, u"Domaine physique")
    ax.legend(loc="upper left")
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

