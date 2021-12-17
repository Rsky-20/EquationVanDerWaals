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


def Isotherme(master):
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
    app.title("Isotherme d'un gaz parfait et d'un gaz de Van Der Waals")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()

    V=np.arange(0.5*pow(10,-4),pow(10,-3),2.5*pow(10,-5))
    T_1=np.arange(300,1301,200)
    def VDW(V,T):
        R=8.314472
        a=363.7*pow(10,-3)
        b=0.0427*pow(10,-3)
        return (T*R/(V-b)-a/(V**2))
    def GP(V,T):
        R=(8.314472)
        return (T*R/V)
    for i in range(0,len(T_1)):
        lab="T"+str(i+1)+"("+str(T_1[i])+"K)"
        ax.plot(V,VDW(V,T_1[i]),color='b',label=lab+'VDW')
    for i in range(0,len(T_1)):
        lab="T"+str(i+1)+"("+str(T_1[i])+"K)"
        ax.plot(V,GP(V,T_1[i]),color='r',label=lab+'GP')
    ax.plot(pow(10,-4),0.725*pow(10,7),'g*',label="Point critique")
    ax.axvline(x=0,color='black')
    ax.axvline(x=4,color='black')
    ax.axhline(y=0,color='black')
    ax.axis([0,1.2*pow(10,-3),0,6*pow(10,7)])
    ax.set_xlabel(r"$V_m\;(m^3.mol^{-1})$")
    ax.set_ylabel(r"$P\;(Pa)$")
    ax.legend(loc="upper right")
    ax.grid(b=True, which='major', color='#666666', linestyle='-')

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

