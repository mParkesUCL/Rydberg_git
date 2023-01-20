'''
Code to calculate the transitions for a Rydberg Atom
'''

#Imports
import const    #file with constants in

#functions


#inputs - hardcode but could come from a file, cli or keyboard input
massAtom = 1    #This is a H atom in amu
zcharge = 1     #The charge of a proton
Rydtype = 1

unit = "cm-1"

n1 = 2  #upper state
n2 = 3  #lower state
nstps = 4   #number of transitions



#convert into correct units
massAtom = massAtom * const.MassA
#calculation

#get Rydberg constant
#need reduced mass

MassR = const.redMass(massAtom, const.MassE)
print("Reduced mass is {0:.4e} kg.".format(MassR))
#Now Rydberg, use Rinf
Rcalc = const.RydCalc(MassR, Rydtype)
print("Calculated Rydberg constant is {0:.4f} cm-1".format(Rcalc))

#do calculation

for value in range(nstps):
    upper = n2 + value  #get n for upper level
    sigma = Rcalc*((1/(n1*n1))-(1/(upper*upper)))
    print("For Transistion {0} to {1} the energy is {2:.4f} {3}".format(upper,n1,sigma, unit))

#outputs
