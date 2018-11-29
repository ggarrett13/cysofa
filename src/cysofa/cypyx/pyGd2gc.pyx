STUFF = 'hi'
import numpy as np

cdef extern from "sofa.h":
    int iauGd2gc ( int n, double elong, double phi, double height,
                   double xyz[3])

def py_iauGd2gc(int n, double elong, double phi, double height):
    #Initialise output matrix
    cdef double xyz[3]

    #Do the C routine, returning the status
    status = iauGd2gc(n, elong, phi, height, xyz)

    #return tuple of xyz array and the status
    return xyz, status