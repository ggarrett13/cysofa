STUFF = "Hi"
import numpy as np

#define the c program Pfw06 as a normal C function
cdef extern from "sofa.h":
    void iauPfw06(double date1, double date2,
              double *gamb, double *phib, double *psib, double *epsa)

#create the python function to use (has 2 inputs for the 2-part date used by sofa. 4 outputs as F-W angles
def py_iauPfw06(double date1, double date2):
    """Wrapper for iauPfw06 module (`SOFA Documentation <http://www.iausofa.org/current_C.html>`_.). For a given date, returns precession angles (Fukushima-Williams 4-angle formulation).

    Args:
      date1 (float): Terrestrial Time as a 2-part Julian Date (Part 1).
      date2 (float): Terrestrial Time as a 2-part Julian Date (Part 2).

    Returns:
      (Numpy Array):

         (1x4) array containing:
            * **gamb** -- F-W angle :math:`\overline{\gamma}` (radians)
            * **phib** -- F-W angle :math:`\overline{\phi}` (radians)
            * **psib** -- F-W angle :math:`\overline{\psi}` (radians)
            * **epsa** -- F-W angle :math:`\overline{\epsilon}` (radians)

    """
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

