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


def EquReduite(master):
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
    app.title("Représentation de l'equation de Van der Waals en coordonnées réduites\n dans le diagramme de Clapeyron")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()

    T_r=np.arange(0.93,1.03,0.01)
    V_r=np.arange(0.4,5,0.01)
    def VDWR(V_R,T_r):
        return (8*T_r)/(3*V_r-1) - (3/(V_r**2))
    for i in range(0,len(T_r)):
        lab="T"+str(i+1)+"("+str(T_r[i])+"K)"
        ax.plot(V_r,VDWR(V_r,T_r[i]),label=lab)
    ax.plot(1,1,'g*',label="Point critique")
    ax.axvline(x=0,color='black')
    ax.axhline(y=0,color='black')
    ax.axis([0.4,2,0.5,1.4])
    ax.set_ylabel(r'$P\;(Pa)$')
    ax.set_xlabel(r'$V_m\;(m^3.mol^{-1})$')
    ax.legend(loc="upper right",fontsize="small")
    ax.set_title("Représentation de l'equation de Van der Waals en coordonnées réduites\n dans le diagramme de Clapeyron")
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

