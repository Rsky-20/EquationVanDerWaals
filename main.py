#!/bin/python3
# -*- coding: utf-8 -*- 
"""[summary]
"""

"""
@Author : Pierre VAUDRY ; Enora GUILLAUME ; Safa HERELLI ; Jessy JESSY
IPSA Aero2 - Prim1
Release date: 15/11/2021

[summary]
Programme principal.

[Functions]:
    fonction_1() - summary
    
[Class]:


[Global variable]:
    {}
        
"""

# --------- Import module section --------- #

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image, ImageTk
import pyscreenshot as ImageGrab #Test / Not working yet
import lib.page1 as Ep
import lib.page2 as Fp
import lib.page3 as GP
import lib.page4 as VDW
import lib.page5 as Iso
import lib.page6 as PT
import lib.page7 as Amag
import lib.page8 as AmagP
import lib.page9 as EqR
import lib.page9Bis as EqRBis
import lib.page10 as MWR
import lib.page11 as MW
import lib.DocumentationHelperAbout as DHA

# --------- Class and process --------- #

class ToolBar:
    """
    [summary]
    ToolBar class make a simple toolbar to dispatch functionalities
    
    [Methode]
    __init__
    top_menu
    quit_app
    """    

    def __init__(self, master):
        """
        [summary]
        initiate class

        Args:
            master (class): tkinter parent page of main app
        """        
        self.root = master # Parent window
        self.top_menu()

    def top_menu(self):
        """
        [summary]
        generate toolbar on the main screen
        """        
        
        menubar = Menu(self.root)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(
            label="Impr. window",
            command=None) #ImageGrab.grab(backend="mss", childprocess=False).save('screen_impr.png')
        menu1.add_separator()
        menu1.add_command(label="Quitter ", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Exercice 1",
                          command=lambda: None)
        menu2.add_command(label="Exercice 2",
                          command=lambda: None)
        menu2.add_command(label="Exercice 3",
                          command=lambda: None)
        menu2.add_command(label="Exercice 4",
                          command=lambda: None)
        
        menubar.add_cascade(label="Informations", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Bienvenue",
                          command=lambda: DHA.BienvenuePage(self.root))
        menu3.add_command(label="A propos",
                          command=lambda: messagebox.showinfo(title="A propos !",
                                                              message=DHA.Apropos))
        menu3.add_command(label="? Aide ?",
                          command=lambda: DHA.HelpPage(self.root))
        menubar.add_cascade(label="Aide", menu=menu3)

        self.root.config(menu=menubar)
        

    def quit_app(self):
        """
        [summary]
        a simple function to stop app / screen
        """        
        
        MessageBox = """
        Voulez-vous quittez l'application ?
        """
        resp = messagebox.askokcancel(
            title="Quitter ThermoSim", message=MessageBox)
        if resp:
            self.root.destroy()
        else:
            pass

class MainApp:
    """
    [description]
    MainApp is the class for generating,
    load and instantiate the base of the management program.
    This class contains the graphical base.
    
    [Methode]
    __init__
    widgets
    admin
    """

    def __init__(self):
        """
        [summary]
        initiate class
        """       
        # Generate the main page with setting
        self.root = tk.Tk()
        self.root.wm_attributes('-transparentcolor', 'red')
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.title("ThermoSim - Equation d'Etat de Van-Der-Waals")
        self.screen = str(self.w)+"x"+str(self.h)
        print(self.screen)
        self.root.geometry(self.screen)
        self.root.resizable(True, True)
        self.root.wm_state(newstate="zoomed")

        # Fullscreen mode
        #self.root.attributes('-fullscreen', 0)

        # Menu : 
        ToolBar(self.root)

        # Background image
        self.image = PhotoImage(file='./img/HomeScreen.png')
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.place(y=-45, x=0, relwidth=1, relheight=2)
        self.canvas.create_image(0, 0, image=self.image, anchor=NW, )
        
        self.banner = Frame(self.root, bg='#ffffff', cursor='circle')
        self.banner.place(y=0,x=0,relwidth=0.25, relheight=1)
        # Icon of window
        self.root.iconbitmap('./img/icon.ico')
        self.widgets()

        self.root.mainloop()

    def widgets(self):
        """
        [description]
        Function containing all the elements of the main page of the program.
        This function gathers all the buttons and interaction objects.

        :return:
        """
        # Button of main functionnalities 
        tk.Button(self.banner, text="Energie d'interaction entre les molecule Ep",
                  command=lambda: Ep.EnergieInteraction(self.root),
                  bg="white").place(relx=0.1, rely=0.05, relheight=0.05, relwidth=0.8)
        tk.Button(self.banner, text="Force d'interaction", command=lambda: Fp.ForceInteraction(self.root),
                  bg="white").place(relx=0.1, rely=0.1, relheight=0.05, relwidth=0.8)
        tk.Button(self.banner, text="Gaz parfait", command=lambda: GP.GazParfait(self.root),
                  bg="white").place( relx=0.1, rely=0.15, relheight=0.05,
                                    relwidth=0.8)
        tk.Button(self.banner, text="Van Der Waals", command=lambda: VDW.VanDerWaals(self.root),
                  bg="white").place( relx=0.1, rely=0.2, relheight=0.05,
                                    relwidth=0.8)
        tk.Button(self.banner, text="Isotherme", command=lambda: Iso.Isotherme(self.root),
                  bg="white").place( relx=0.1, rely=0.25, relheight=0.05,
                                    relwidth=0.8)
        tk.Button(self.banner, text="Pression T", command=lambda: PT.Pression_T(self.root),
                  bg="white").place( relx=0.1, rely=0.3, relheight=0.05,
                                    relwidth=0.8)
        tk.Button(self.banner, text="Amagat", command=lambda: Amag.Amagat(self.root),
                  bg="white").place( relx=0.1, rely=0.35, relheight=0.05,
                                    relwidth=0.8)          
        tk.Button(self.banner, text="Amagat P", command=lambda: AmagP.AmagatP(self.root),
                  bg="white").place( relx=0.1, rely=0.40, relheight=0.05,
                                    relwidth=0.8) 
        tk.Button(self.banner, text="Equation Reduite", command=lambda: EqR.EquReduite(self.root),
                  bg="white").place( relx=0.1, rely=0.45, relheight=0.05,
                                    relwidth=0.8) 
        tk.Button(self.banner, text="Equation Reduite Custom", command=lambda: EqRBis.EquReduite(self.root),
                  bg="white").place( relx=0.1, rely=0.50, relheight=0.05,
                                    relwidth=0.8) 
        tk.Button(self.banner, text="Construction de Maxwell Réduit", command=lambda: MWR.ConstuctionMaxwell(self.root),
                  bg="white").place( relx=0.1, rely=0.55, relheight=0.05,
                                    relwidth=0.8)
        tk.Button(self.banner, text="Construction de Maxwell", command=lambda: MW.ConstuctionMaxwell(self.root),
                  bg="white").place( relx=0.1, rely=0.6, relheight=0.05,
                                    relwidth=0.8)


# ------ Run & Start server program ------ #

if __name__ == '__main__':
    print(__doc__)

    # Run the program
    app = MainApp()
