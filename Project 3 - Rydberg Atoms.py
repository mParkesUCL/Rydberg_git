'''
Script to calculate Electronic transistion
for Hydrogenic ions
'''

#imports here
import module
from sys import argv #this is the CLI
import argparse #this is better CLI

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

#input - hard code for now, come back and fix
def input(parsed_args):
    '''
    get inputs
    type can be 0 hardcode (test)
        1   from file
        2 from cli
        etc
    '''
    #print(argv)

    #type = int(argv[1])
    type = parsed_args.input_type
    if type == 0:
        atomMass = 1    #hydrogen atom in amu
        atomcharge = 1  #hydrogen charge
        unit = "cm-1"
        n1 = 2
        n2 = 3

        nsteps = 4
        #add other input types
        #Get from a file
        print(parsed_args.filename)
    elif type ==2:
        #Get from CLI options
        print("Set up CLI")
        print("More changes")
        atomMass = parsed_args.mass
        atomcharge = parsed_args.charge
        unit = parsed_args.unit
        n1 = parsed_args.n1
        n2 = parsed_args.n2
        nsteps = parsed_args.steps
    return atomMass,atomcharge,unit,n1,n2, nsteps


#print(input(0))
parse = parser()
parsed_args = parse.parse_args()
print(parsed_args)
atomMass,atomcharge,unit,n1,n2, nsteps = input(parsed_args)
#calculation
#calculate Reduced mass
massR = module.redmass(atomMass*module.MassA,module.MassE)
print("Reduced mass is {0:.4e} kg".format(massR))
#calculate Rydberg constant
Ryd = module.rydcalc(massR,1)
print("Rydberg constant {0:.4f} cm-1".format(Ryd))
#loop
    #calculate the transition energy
for value in range(nsteps):
    upper = n2 + value
    sigma = (atomcharge*atomcharge)*Ryd*((1/(n1*n1))-(1/(upper*upper)))
    print("For transition {0} -> {1} energy {2} {3}".format(n1,upper,sigma,unit))

#output -somehow