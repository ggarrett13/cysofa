STUFF = 'hi'
import numpy as np

cdef extern from "sofa.h":
    void iauC2t00a(double tta, double ttb, double uta, double utb,
               double xp, double yp, double rc2t[3][3])

def py_iauC2t00a(double tta, double ttb, double uta, double utb, double xp, double yp):
    cdef double rc2t[3][3]  #initialise C array

    iauC2t00a(tta, ttb, uta, utb, xp, yp, rc2t)     #perform sofa routine

    return np.array(rc2t)   #return the array as a numpy object

