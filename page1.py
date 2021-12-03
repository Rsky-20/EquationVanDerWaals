import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

info = "test"

def EnergieReduiteRepulsive(R): 
    return (1 / R) ** 12

def EnergieReduiteAttractive(R): 
    return -2 * ((1 / R) ** 6)

def EnergieInteractionReduiteTotale(R):
    return (EnergieReduiteRepulsive(R) + EnergieReduiteAttractive(R))    
    

def exercice1(master):
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
    app.title("Exercice 1")

    label = tk.LabelFrame(app, text="Sélectionnez l'utilisateur dont vous voulez annuler la réservation")
    label.place(relheight=1, relwidth=1)
    
    fig = Figure(figsize=(5, 4), dpi=100)

    x = [p/100.0 for p in range(50, 250, 1)]
    y = []
    y_ERA = [] #Energie Reduit d'attraction
    y_ERR = [] #Energie Reduite de Repulsion
    y_EIRT = [] #Energie d'Interaction Reduite Totale
    y = []

    for j in range(len(x)):
        y.append(0)
        distIMR = x[j] #Distance Inter Moleculaire Reduite
        ERA = EnergieReduiteAttractive(distIMR)
        y_ERA.append(ERA)
        ERR = EnergieReduiteRepulsive(distIMR)
        y_ERR.append(ERR)
        EIRT = EnergieInteractionReduiteTotale(distIMR)
        y_EIRT.append(EIRT)


    ax = fig.add_subplot()
    line, = ax.plot(x, y,color="black", linewidth=1, linestyle="-")
    line1, = ax.plot(x, y_ERR, linewidth=2.5, linestyle="-", label="Energie réduite de repulsion")
    repulsive = ax.axvspan(0.5, 1, facecolor='r', alpha=0.2, label='zone repulsive')
    line2, = ax.plot(x, y_ERA, linewidth=2.5, linestyle="-", label="Energie  réduite d'attraction")
    attractive = ax.axvspan(1, 2, facecolor='b', alpha=0.2, label='zone attractive')
    line3, = ax.plot(x, y_EIRT, linewidth=2.5, linestyle="-", label="Energie d'interaction réduite totale")
    total = ax.axvspan(2, 2.5, facecolor='g', alpha=0.2, label='zone sans interaction')

    #ax.title("Potentiel de Lennard Jones") 
    ax.set_xlim(0.5,2.5)
    ax.set_ylim(-1.5,1.5)
    ax.set_xlabel("time [s]")
    ax.set_ylabel("f(t)")

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

    userInfo = tk.Text(label)
    userInfo.insert(tk.END,info)
    userInfo.place(relx=0.3, rely=0.15, relheight=0.6, relwidth=0.4)
