'''
Module with functions for Rydberg
'''

charge = 1.602E-19 #fundamental charge in C
epsi0 = 8.854E-12 #permitivity of free space in F m -1
planck = 6.626E-34 #planck's constant in J s
speC = 2.998E8 #speed of light in m s-1
MassE = 9.109E-31 #masss of an electron in kg
MassA = 1.6605E-27 #mass of an atomic unit in kg
Rinf = 109737 #R infinity in cm-1

def redmass(m1,m2):
    '''
    Function will calculate reduced mass of two things
    m1 and m2 are floats
    Must be in same mass units
    '''

    redmass = (m1*m2)/(m1+m2)

    return redmass

def rydcalc(redmass,rtype):
    '''
    Calculate Ryderg constant for hydrogenic atom
    of reduced mass redmass

    rtype select calc method, 1 use Rinf, 2 use constants
    '''

    if rtype == 1:
        #calculate from Rinf
        rcalc = (redmass/MassE)*Rinf
    else:
        #nothing selected, shouldn't happen
        rcalc = -1
    
    return rcalc