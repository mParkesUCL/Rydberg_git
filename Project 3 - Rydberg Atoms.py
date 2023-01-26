'''
Script to calculate Electronic transistion
for Hydrogenic ions
'''

#imports here
import module

#input - hard code for now, come back and fix
def input(type):
    '''
    get inputs
    type can be 0 hardcode (test)
        1   from file
        2 from cli
        etc
    '''
    if type == 0:
        atomMass = 1    #hydrogen atom in amu
        atomcharge = 1  #hydrogen charge
        unit = "cm-1"
        n1 = 2
        n2 = 3

        nsteps = 4
        #add other input types
    elif type ==1:
        print("Set up CLI")
        print("More changes")
    return atomMass,atomcharge,unit,n1,n2, nsteps


print(input(0))
atomMass,atomcharge,unit,n1,n2, nsteps = input(0)
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