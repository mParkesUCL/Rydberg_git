'''
Module with functions for Rydberg
'''
import argparse #this is better CLI

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

def parser():
    '''
    Sets up and returns the parser
    '''

    parse = argparse.ArgumentParser(description='Calculate the Electronic transitions of Hydrogenic Atoms')

    parse.add_argument('input_type',
                        type = int,
                        help = "Where the inputs are coming from, 0 is hardcoded to H atom,\
                            1 is from a file - must give filename\
                            2 is from the CLI options")
    parse.add_argument('-mass',
                       type = float,
                       help = "The mass of the atom to use in the calculation.\
                        Defaults to 1.0 (H atom)",
                        default=1.0)
    parse.add_argument("-charge",
                       type = int,
                       help="The charge of the Hydrogenic atom.\
                        Defaults to +1",
                        default=1)
    parse.add_argument("-unit",
                       type=str,
                       help="The unit that is in use - currently cosmetic.\
                        Defaults to cm-1",
                        default="cm-1")
    parse.add_argument("-n1",
                       type = int,
                       help= "The lower state to be used in the calculation.\
                        Defaults to 2 (Balmer series)",
                        default=2)
    parse.add_argument("-n2",
                       type=int,
                       help="Initial upper state to be used in the calculation\
                        Defaults to 3, should be greater than n1",
                        default=3)
    parse.add_argument("-steps",
                       type=int,
                       help="The number of steps to make in calculation.\
                        Defaults to 1",
                        default=1)
    parse.add_argument("-filename",
                       type=str,
                       help="File to load the settings from. Only useful when combined with type = 1. No default")
    return parse