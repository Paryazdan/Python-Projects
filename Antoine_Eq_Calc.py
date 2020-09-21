import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def AntoineEq(T,X):
    p = []
    if X == 1:
        for i in T:
            p.append(10**(bA-(bB/(i+bC))))
    elif X == 0:
        for i in T:
            p.append(10**(tA-(tB/(i+tC))))
    else:
        global pB, pT
        for i in range(0,len(T)):
            p.append(0.4*pB[i]+0.6*pT[i])
    return p
def bpTemp(bp):
    print('''The bubble point temperature of a 40 mol%
Benzene and 60 mol% Toluene mixture is '''+str(bp)+" deg C")
def Pvap(T):
    return 0.4*(10**(bA-(bB/(T+bC))))+0.6*(10**(tA-(tB/(T+tC)))) - Ptotal
Temps = []
for i in range(0,201,10): #Creating a list of temperatures from 0 to 200
    Temps.append(i)
#Antoine Equation constants for Benzene and Toluene
bA = 6.89272
bB = 1203.531
bC = 219.888
tA = 6.95805
tB = 1346.773
tC = 219.693
#Calculation of vapor pressures
pB = [] #Pure Benzene
pT = [] #Pure Toluene
pMix = [] #40 mol% Benzene and 60 mol% Toluene
pB = AntoineEq(Temps,1)
pT = AntoineEq(Temps,0)
pMix = AntoineEq(Temps,2)
plt.plot(Temps, pB, label="Pure Benzene")
plt.plot(Temps, pT, label="Pure Toluene")
plt.plot(Temps, pMix, label="40 mol% Benzene and 60 mol% Toluene")
plt.xlabel("Temperature (degrees Celsius)")
plt.ylabel("Vapor Pressure (mm Hg)")
plt.title("Vapor pressures of Benzene and Toluene at various Temperatures")
plt.legend()
plt.show()
#Calulating bubble point temp of 750 mmHg of the mixture
Tguess = 110
Ptotal = 750
x = fsolve(Pvap,Tguess)
bpTemp(x)
