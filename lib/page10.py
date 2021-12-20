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
from scipy.integrate import quad
from scipy.optimize import newton
from scipy.signal import argrelextrema


def ConstuctionMaxwell(master):
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
    app.title("Isotherme réduit d'un gaz de VDW")
    
    fig = Figure(figsize=(5, 4), dpi=100)

    ax = fig.add_subplot()

    T_r=np.arange(0.93, 1.03, 0.01)
    V_r=np.arange(0.4, 5, 0.01)
    
    palette = iter(['#9b59b6', '#4c72b0', '#55a868', '#c44e52', '#dbc256', '#94331E',
                    '#1E9484', '#25941E','#948F1E', '#1E3994', '#941E44'])

    # Critical pressure, volume and temperature
    # These values are for the van der Waals equation of state for CO2:
    # (p - a/V^2)(V-b) = RT. Units: p is in Pa, Vc in m3/mol and T in K.
    pc = 7.404e6
    Vc = 1.28e-4
    Tc = 304

    def vdw(Tr, Vr):
        """Van der Waals equation of state.

        Return the reduced pressure from the reduced temperature and volume.

        """

        pr = 8*Tr/(3*Vr-1) - 3/Vr**2
        return pr


    def vdw_maxwell(Tr, Vr):
        """Van der Waals equation of state with Maxwell construction.

        Return the reduced pressure from the reduced temperature and volume,
        applying the Maxwell construction correction to the unphysical region
        if necessary.

        """

        pr = vdw(Tr, Vr)
        if Tr >= 1:
            # No unphysical region above the critical temperature.
            return pr

        if min(pr) < 0:
            raise ValueError('Negative pressure results from van der Waals'
                            ' equation of state with Tr = {} K.'.format(Tr))

        # Initial guess for the position of the Maxwell construction line:
        # the volume corresponding to the mean pressure between the minimum and
        # maximum in reduced pressure, pr.
        iprmin = argrelextrema(pr, np.less)
        iprmax = argrelextrema(pr, np.greater)
        Vr0 = np.mean([Vr[iprmin], Vr[iprmax]])

        def get_Vlims(pr0):
            """Solve the inverted van der Waals equation for reduced volume.

            Return the lowest and highest reduced volumes such that the reduced
            pressure is pr0. It only makes sense to call this function for
            T<Tc, ie below the critical temperature where there are three roots.

            """

            eos = np.poly1d( (3*pr0, -(pr0+8*Tr), 9, -3) )
            roots = eos.r
            roots.sort()
            Vrmin, _, Vrmax = roots
            return Vrmin, Vrmax

        def get_area_difference(Vr0):
            """Return the difference in areas of the van der Waals loops.

            Return the difference between the areas of the loops from Vr0 to Vrmax
            and from Vrmin to Vr0 where the reduced pressure from the van der Waals
            equation is the same at Vrmin, Vr0 and Vrmax. This difference is zero
            when the straight line joining Vrmin and Vrmax at pr0 is the Maxwell
            construction.

            """

            pr0 = vdw(Tr, Vr0)
            Vrmin, Vrmax = get_Vlims(pr0)
            return quad(lambda vr: vdw(Tr, vr) - pr0, Vrmin, Vrmax)[0]

        # Root finding by Newton's method determines Vr0 corresponding to
        # equal loop areas for the Maxwell construction.
        Vr0 = newton(get_area_difference, Vr0)
        pr0 = vdw(Tr, Vr0)
        Vrmin, Vrmax = get_Vlims(pr0)

        # Set the pressure in the Maxwell construction region to constant pr0.
        pr[(Vr >= Vrmin) & (Vr <= Vrmax)] = pr0
        return pr

    Vr = np.linspace(0.5, 3, 500)

    def plot_pV(T):
        Tr = T / Tc
        c = next(palette)
        ax.plot(Vr, vdw(Tr, Vr), lw=2, alpha=0.3, color=c)
        ax.plot(Vr, vdw_maxwell(Tr, Vr), lw=2, color=c, label='{:.2f}'.format(Tr))


    for T in range(270, 320, 5):
        plot_pV(T)

    ax.set_xlim(0.4, 4)
    ax.set_xlabel('Reduced volume')
    ax.set_ylim(0, 2)
    ax.set_ylabel('Reduced pressure')    
    ax.axvline(x=0, color='black')
    ax.axhline(y=0, color='black')
    ax.axis([0.4, 4, 0, 2])
    ax.legend(loc="upper right",fontsize="small",title='Reduced temperature')
    ax.set_title("Isotherme réduit d'un gaz de VDW")
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

