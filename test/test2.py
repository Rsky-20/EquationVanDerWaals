import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


def EnergieReduiteRepulsive(R): 
    return (1 / R) ** 12

def EnergieReduiteAttractive(R): 
    return -2 * ((1 / R) ** 6)

def EnergieInteractionReduiteTotale(R):
    return (EnergieReduiteRepulsive(R) + EnergieReduiteAttractive(R))


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

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

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tkinter.Button(master=root, text="Quit", command=root.quit)

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button_quit.pack(side=tkinter.BOTTOM)
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()