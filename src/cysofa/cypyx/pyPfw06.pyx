STUFF = "Hi"
import numpy as np

#define the c program Pfw06 as a normal C function
cdef extern from "sofa.h":
    void iauPfw06(double date1, double date2,
              double *gamb, double *phib, double *psib, double *epsa)

#create the python function to use (has 2 inputs for the 2-part date used by sofa. 4 outputs as F-W angles
def py_iauPfw06(double date1, double date2):
    #Initialise the F-W angles as any number (just used to give them a memory location really)
    cdef double gamb
    cdef double phib
    cdef double psib
    cdef double epsa

    #Assign each F-W angle a pointer to feed to the C function
    cdef double* pgamb = &gamb
    cdef double* pphib = &phib
    cdef double* ppsib = &psib
    cdef double* pepsa = &epsa

    #Use the C function to directly modify the value of each F-W angle in it's memory location
    iauPfw06(date1, date2,
              pgamb, pphib, ppsib, pepsa)

    return np.array([gamb, phib, psib, epsa])

