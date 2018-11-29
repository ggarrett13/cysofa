STUFF = 'hi'
import numpy as np

cdef extern from "sofa.h":
    void iauPn00a(double date1, double date2,
              double *dpsi, double *deps, double *epsa,
              double rb[3][3], double rp[3][3], double rbp[3][3],
              double rn[3][3], double rbpn[3][3])

def py_iauPn00a(double date1, double date2):

    #Initialise 3 variables pointed to
    cdef double dpsi
    cdef double deps
    cdef double epsa

    #Initialise pointers for the 3 variables
    cdef double* pdpsi = &dpsi
    cdef double* pdeps = &deps
    cdef double* pepsa = &epsa

    #Initialise remaining output variables
    cdef double rb[3][3]
    cdef double rp[3][3]
    cdef double rbp[3][3]
    cdef double rn[3][3]
    cdef double rbpn[3][3]

    #execute C subroutine
    iauPn00a(date1, date2,
              pdpsi, pdeps, pepsa,
              rb, rp, rbp,
              rn, rbpn)

    #Convert C arrays to numpy arrays
    np_rb = np.array(rb)
    np_rp = np.array(rp)
    np_rbp = np.array(rbp)
    np_rn = np.array(rn)
    np_rbpn = np.array(rbpn)

    #Return python tuple of output variables
    return np_rb, np_rp, np_rbp, np_rn, np_rbpn