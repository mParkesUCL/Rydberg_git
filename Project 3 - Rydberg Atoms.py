'''
Script to calculate Electronic transistion
for Hydrogenic ions
'''

#imports here
import module


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
parse = module.parser()
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