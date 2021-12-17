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

def Fpi(r):
        return (12*(1/r)**13 - 12*(1/r)**7)
def Fea(r):
    return (-12*(1/r)**7)
def Fer(r):
    return (12*(1/r)**13)

def ForceInteraction(master):
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
    app.title(r"Forces d'interaction en fonction de $(r/r_0)$")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    #x = [p/100.0 for p in range(50, 250, 1)]
    x=np.arange(-20,20.1,0.0001) 


    ax = fig.add_subplot()
    ax.plot(x,Fpi(x),"g",label=r'$\frac{F}{F_0}(r/r_0)$')
    ax.axvline(x=0,color='black')
    ax.axhline(y=0,color='black')
    ax.set_xlim(0.5,2.5)
    ax.set_ylim(-1.5,1.5)
    ax.axis([0.5,2.5,-6,6])
    ax.plot(x,Fea(x),'r',label='$F_{EA}(r/r_0)$')
    ax.plot(x,Fer(x),'b',label='$F_{ER}(r/r_0)$')
    ax.legend(loc='upper right')
    ax.set_xlabel('$(r/r_0)$')
    ax.set_ylabel('$F/F_0$')
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

