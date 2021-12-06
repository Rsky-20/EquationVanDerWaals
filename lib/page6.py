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


def Pression_T(master):
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
    app.title("Représentation de la pression en fonction de la température \n pour le CO₂ en tant que gaz parfait et de Van Der Waals")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()

    T=np.arange(300,1301,10)
    V=np.arange(2*pow(10,-4),pow(10,-3),2*pow(10,-4))
    def VDW(V,T):
        R=8.314472
        a=363.7*pow(10,-3)
        b=0.0427*pow(10,-3)
        return (T*R/(V-b)-a/(V**2))
    def GP(V,T):
        R=(8.314472)
        return (T*R/V)
    for i in range(0,len(V)):
        lab="V"+str(i+1)
        ax.plot(T,VDW(V[i],T),color='b',label=lab +'VDW')
    for i in range(0,len(V)):
        lab="V"+str(i+1)
        ax.plot(T,GP(V[i],T),color='r',label=lab+'GP')
    ax.set_xlabel(r"Température (K)")
    ax.set_ylabel(r"Pression (Pa)")
    ax.axis([200,1400,0,7*pow(10,7)])
    ax.legend(loc="upper left",fontsize="small")
    

    canvas = FigureCanvasTkAgg(fig, master=app)  # A tk.DrawingArea.
    canvas.draw()

    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, app, pack_toolbar=False)
    toolbar.update()

    canvas.mpl_connect(
        "key_press_event", lambda event: print(f"you pressed {event.key}"))
    canvas.mpl_connect("key_press_event", key_press_handler)

    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

