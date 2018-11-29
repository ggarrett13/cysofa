#module used for command line interactions
import subprocess
import numpy as np
import time

build=True
if build:
    #use 'make' in proper directories to compile the c files into a static librayr
    subprocess.call(['make']) #run outer makefile
    subprocess.call(['make', 'tidy']) #run outer makefile

#import the library
#from cysofa import pyanp, pyPfw06, pyC2t00a, pyPn00a, pyGd2gc
from cypyx import pyanp, pyPfw06, pyC2t00a, pyPn00a, pyGd2gc
from cysofa import utils

#run an example of pyanp
a = np.double(6.7)
newa = pyanp.py_iauAnp(a)
print(pyanp.py_iauAnp(a), type(newa))

#run an example of pyPfw06
date1 = 2450124.7
date2 = 0.0
newd = pyPfw06.py_iauPfw06(date1, 0.)#, 0., 0., 0., 0.)
print(newd, type(newd))
print(np.rad2deg(newd))

#run an example of pyC2t00a
tdate1 = 2450124.7
tdate2 = 0.0
utdate1 = 2450124.7 +12
utdate2 = 0.0
xp = 0.75
yp = 1.6
newc = pyC2t00a.py_iauC2t00a(tdate1, tdate2, utdate1, utdate2, xp, yp)
print(newc, type(newc))

#run an example of pyPn00a
pndate1 = 2450124.7
pndate2 = 0.0
newPn = pyPn00a.py_iauPn00a(pndate1, pndate2)
print(newPn, type(newPn))

#run an example of Gd2gc
n = 3
elong = 56.3
phi = 1.27
height = 1000.5

newGd = pyGd2gc.py_iauGd2gc(n, elong, phi, height)
print(newGd, type(newGd))




#kill the makefiles if you want
#kill = True
kill = False
if kill == True:
    subprocess.call(['make', 'clean'])
