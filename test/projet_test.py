import numpy as np
import  matplotlib.pyplot as plt
#-----------------------------------------------------------
x=np.arange(-20,20.1,0.0001) 
def Ep ():
    def Ea (r):  
        return (-2*(1/r)**6)
    def Er(r): 
        return ((1/r)**12)
    def Epi(r): 
        return ((1/r)**12 - 2*(1/r)**6)
    plt.plot(x,Epi(x),'g',label=r'$\frac{E_{p\; i}}{\epsilon}$')
    plt.axvline(x=0,color='black')  
    plt.axhline(y=0,color='black') 
    plt.xlim(0.5,2.5) 
    plt.ylim(-1.5,1.5)
    plt.axis([0.5,2.5,-6,6])
    plt.plot(x,Ea(x),'r',label=r'$E_{a}(r)$')
    plt.plot(x,Er(x),'b',label=r'$E_r(r)$')
    plt.legend(loc='upper right',fontsize=14)
    plt.title(r"Potentiel de Lennard-Jones en fonction de $\frac{r}{r_0}$")
    plt.xlabel(r'$\frac{r}{r_0}$')
    plt.ylabel('Energies potentielles')
    plt.grid() 
    plt.savefig('Energies_potentielles.png')
    plt.show() 
    plt.clf() 
#-----------------------------------------------------------
def forceinteraction():
    def Fpi(r):
        return (12*(1/r)**13 - 12*(1/r)**7)
    def Fea(r):
        return (-12*(1/r)**7)
    def Fer(r):
        return (12*(1/r)**13)
    plt.plot(x,Fpi(x),"g",label=r'$\frac{F}{F_0}(r/r_0)$')
    plt.axvline(x=0,color='black')
    plt.axhline(y=0,color='black')
    plt.xlim(0.5,2.5)
    plt.ylim(-1.5,1.5)
    plt.axis([0.5,2.5,-6,6])
    plt.plot(x,Fea(x),'r',label='$F_{EA}(r/r_0)$')
    plt.plot(x,Fer(x),'b',label='$F_{ER}(r/r_0)$')
    plt.legend(loc='upper right')
    plt.title("Forces d'interaction en fonction de $(r/r_0)$")
    plt.xlabel('$(r/r_0)$')
    plt.ylabel('$F/F_0$')
    plt.grid()
    plt.savefig('force_interaction.png')
    plt.show()
    plt.clf()
#-----------------------------------------------------------
def GazParfait():
    x=np.arange(-20,20.1,0.0001)
    T=np.arange(0.5,3.6,0.5)
    def GP(V,T):
        R=(8.314472)
        return (T*R/V)
    for i in range(0,len(T)):
        L="T"+str(i+1)+"(K)"
        plt.plot(x,GP(x,T[i]),linewidth=1,label=L)
    plt.axvline(x=0,color='black')
    plt.axhline(y=0,color='black')
    plt.axis([-20,20,-20,20])
    plt.title("Représentation graphique mathématique de l'équation des gaz parfaits")
    plt.ylabel('P (Pa)')
    plt.xlabel(r"$V_m\; (m^3.mol^{-1})$")
    plt.grid()
    plt.text(7,9,u"Domaine physique")
    plt.legend(loc="upper left")
    plt.savefig("GazParfait.PNG")
    plt.show()
    plt.clf()
#-----------------------------------------------------------
def VanDerWaals():
    x=np.arange(-20,20.1,0.0001)
    T=np.arange(0.5,3.6,0.5)
    def VDW(V,T):
        a=1
        b=4
        R=8.314472
        return (T*R/(V-b) - a/(V**2))
    for i in range(0,len(T)):
        L="T"+str(i+1)+"("+str(T[i])+"K)"
        plt.plot(x,VDW(x,T[i]),label=L)
    plt.axvline(x=0,color='black')
    plt.axvline(x=4,color='black',linewidth=0.3)
    plt.axhline(y=0,color='black')
    plt.axis([-15,15,-15,15])
    plt.title("Représentation de l'equation mathématique de Van der Waals")
    plt.ylabel(r"$P\;(Pa)$")
    plt.xlabel(r"$V_m\;(m^3.mol^{-1})$")
    plt.grid()    
    plt.legend(loc='upper left')
    plt.axhspan(-15,0,color='orange',alpha=0.3)
    plt.axvspan(-15,4,color='orange',alpha=0.3)
    plt.text(7.8,12,u'Domaine')
    plt.text(7.8,10.8,u'physique')
    plt.savefig("VDW.PNG")
    plt.show()
    plt.clf()
#-----------------------------------------------------------
def Isotherme():
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
        plt.plot(V,VDW(V,T_1[i]),color='b',label=lab+'VDW')
    for i in range(0,len(T_1)):
        lab="T"+str(i+1)+"("+str(T_1[i])+"K)"
        plt.plot(V,GP(V,T_1[i]),color='r',label=lab+'GP')
    plt.plot(pow(10,-4),0.725*pow(10,7),'g*',label="Point critique")
    plt.axvline(x=0,color='black')
    plt.axvline(x=4,color='black')
    plt.axhline(y=0,color='black')
    plt.axis([0,1.2*pow(10,-3),0,6*pow(10,7)])
    plt.title("Isotherme d'un gaz parfait et d'un gaz de Van Der Waals")
    plt.xlabel(r"$V_m\;(m^3.mol^{-1})$")
    plt.ylabel(r"$P\;(Pa)$")
    plt.legend(loc="upper right")
    plt.grid()
    plt.savefig('Isotherme_dun_GP_et_de_VDW.png')
    plt.show()
    plt.clf()
#-----------------------------------------------------------
def Pression_T():
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
        plt.plot(T,VDW(V[i],T),color='b',label=lab +'VDW')
    for i in range(0,len(V)):
        lab="V"+str(i+1)
        plt.plot(T,GP(V[i],T),color='r',label=lab+'GP')
    plt.title("Représentation de la pression en fonction de la température \n pour le CO₂ en tant que gaz parfait et de Van Der Waals")
    plt.xlabel(r"Température (K)")
    plt.ylabel(r"Pression (Pa)")
    plt.axis([200,1400,0,7*pow(10,7)])
    plt.grid()
    plt.legend(loc="upper left",fontsize="small")
    plt.savefig("Pression_température_CO₂.png")
    plt.show()
    plt.clf()
#-----------------------------------------------------------
def Amagat():
    V=np.arange(0.05*pow(10,-3),0.1,pow(10,-6))
    T=np.arange(300,1301,200)
    def VDWCO_2(V,T):
        R=8.314472
        a=363.7*pow(10,-3)
        b=0.0427*pow(10,-3)
        return (T*R/(V-b)-a/(V**2))
    def GP(V,T):
        R=(8.314472)
        return (T*R/V)
    def GPAmagat(V,T):
        R=8.314472
        return (GP(V,T)*V)
    def VDWCO_2Amagat(V,T):
        return (VDWCO_2(V,T)*V)
    for i in range(0,len(T)):
        lab="T"+str(i+1)+"("+str(T[i])+"K) VDW"
        plt.plot(VDWCO_2(V,T[i]),VDWCO_2Amagat(V,T[i]),color='b',label=lab)
    for i in range(0,len(T)):
        lab="T"+str(i+1)+"("+str(T[i])+"K) GP"
        plt.plot(GP(V,T[i]),GPAmagat(V,T[i]),color='r',label=lab)
    plt.axis([0,2.5*pow(10,7),0,9*pow(10,3)])
    plt.title("Coordonnées d'Amagat : PV en fonction de P")
    plt.ylabel(r'$PV\;(Pa.m^3)$')
    plt.xlabel(r'$P\;(Pa)$')
    plt.grid()
    plt.savefig("Amagat.png")
    plt.show()
#-----------------------------------------------------------
def AmagatP():
    V=np.arange(0.05*pow(10,-3),0.1,pow(10,-6))
    T=np.arange(300,1301,200)
    PVm=np.arange(0,9001,1)
    Pm=[]
    a=363.7*pow(10,-3)
    b=0.0427*pow(10,-3)
    def VDW(V,T):
        R=8.314472
        return (T*R/(V-b)-a/(V**2))
    def GP(V,T):
        R=(8.314472)
        return (T*R/V)
    def GPAmagat(V,T):
        R=8.314472
        return (GP(V,T)*V)
    def VDWAmagat(V,T):
        return (VDW(V,T)*V)
    for i in range(0,len(T)):
        plt.plot(VDW(V,T[i]),VDWAmagat(V,T[i]),color='b')
    for i in range(0,len(T)):
        lab="T"+str(i+1)+"GP"
        plt.plot(GP(V,T[i]),GPAmagat(V,T[i]),color='r')
    for i in range(len(PVm)):
        Pm.append(-PVm[i]/2 * (PVm[i]/a - 1/b))
    plt.plot(Pm,PVm,color='green')
    plt.axis([0,3*pow(10,7),0,9*pow(10,3)])
    plt.title("Coordonnées d'Amagat : PV en fonction de P \n Parabole de Mariotte Gaz de Van Der Waals CO2")
    plt.ylabel(r'$PV\;(Pa.m^3)$')
    plt.xlabel(r'$P\;(Pa)$')
    plt.grid()
    plt.savefig("AmagatP.png")
    plt.show()
    plt.clf()
#-----------------------------------------------------------
def EquReduite():
    T_r=np.arange(0.93,1.03,0.01)
    V_r=np.arange(0.4,5,0.01)
    def VDWR(V_R,T_r):
        return (8*T_r)/(3*V_r-1) - (3/(V_r**2))
    for i in range(0,len(T_r)):
        lab="T"+str(i+1)+"("+str(T_r[i])+"K)"
        plt.plot(V_r,VDWR(V_r,T_r[i]),label=lab)
    plt.plot(1,1,'g*',label="Point critique")
    plt.axvline(x=0,color='black')
    plt.axhline(y=0,color='black')
    plt.axis([0.4,2,0.5,1.4])
    plt.ylabel(r'$P\;(Pa)$')
    plt.xlabel(r'$V_m\;(m^3.mol^{-1})$')
    plt.title("Représentation de l'equation de Van der Waals en coordonnées réduites\n dans le diagramme de Clapeyron")
    plt.legend(loc="upper right",fontsize="small")
    plt.savefig("EquReduite.png")
    plt.grid()
    plt.show()
    plt.clf()
    
EquReduite()
#-----------------------------------------------------------