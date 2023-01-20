'''
Useful Constants
'''

charge = 1.602E-19 #fundamental charge in C
epsi0 = 8.854E-12 #permitivity of free space in F m -1
planck = 6.626E-34 #planck's constant in J s
speC = 2.998E8 #speed of light in m s-1
MassE = 9.109E-31 #masss of an electron in kg
MassA = 1.6605E-27 #mass of an atomic unit in kg
Rinf = 109737 #R infinity in cm-1

def redMass(m1,m2):
    '''
    Calculate the reduced mass of the m1, m2 system
    mu = (m1 * m2)/(m1 + m2)
    m1 and m2 are floats
    must be in same units for calculation to work
    '''

    redM = (m1*m2)/(m1+m2)

    return redM

def RydCalc(Redmass, Rtype):
    '''
    calculate the Rydberg constant for a given system
    Requires:
    Redmass      Reduced mass of system in kg
    Rtype       How to calculate constant, 1 is Rinf, 2 is full formula

    '''
    if Rtype == 1:
        #Rinf
        Rcalc = (Redmass/MassE)*Rinf
    else:
        #No selection, shouldn't happen
        Rcalc = -1
    
    return Rcalc