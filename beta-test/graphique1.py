import matplotlib.pyplot as plt
def EnergieReduiteRepulsive(R): 
    return (1 / R) ** 12

def EnergieReduiteAttractive(R): 
    return -2 * ((1 / R) ** 6)

def EnergieInteractionReduiteTotale(R):
    return (EnergieReduiteRepulsive(R) + EnergieReduiteAttractive(R))

def Draw_my_function():
    print("gg")
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
        
    plt.title("Potentiel de Lennard Jones") 
    plt.xlim(0.5,2.5)
    plt.ylim(-1.5,1.5)
    axe = plt.gca()
    axe.spines['right'].set_color('none')
    axe.spines['top'].set_color('none')
    axe.xaxis.set_ticks_position('bottom')
    #axe.spines['bottom'].set_position(('data',0))
    #axe.spines['left'].set_position(('data',0.5))

    plt.plot(x, y,color="black", linewidth=1, linestyle="-")
    plt.plot(x, y_ERR, linewidth=2.5, linestyle="-", label="Energie réduite de repulsion")
    repulsive = plt.axvspan(0.5, 1, facecolor='r', alpha=0.2, label='zone repulsive')
    plt.plot(x, y_ERA, linewidth=2.5, linestyle="-", label="Energie  réduite d'attraction")
    attractive = plt.axvspan(1, 2, facecolor='b', alpha=0.2, label='zone attractive')
    plt.plot(x, y_EIRT, linewidth=2.5, linestyle="-", label="Energie d'interaction réduite totale")
    total = plt.axvspan(2, 2.5, facecolor='g', alpha=0.2, label='zone sans interaction')

    plt.legend(loc='upper right')
    axe.set_xlabel('r/r0')
    axe.set_ylabel('Ep(r)/e')

    figure = plt.Figure(figsize=(6, 4), dpi=96)

    plt.savefig('figure')
    plt.show
    
    return figure
