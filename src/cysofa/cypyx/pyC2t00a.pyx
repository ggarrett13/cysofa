STUFF = 'hi'
import numpy as np

cdef extern from "sofa.h":
    void iauC2t00a(double tta, double ttb, double uta, double utb,
               double xp, double yp, double rc2t[3][3])

def py_iauC2t00a(double tta, double ttb, double uta, double utb, double xp, double yp):
    """Wrapper for iauC2t00a module (`SOFA Documentation <http://www.iausofa.org/current_C.html>`_.). Converts from celestial to terrestrial matrix given the date, UT1 and Polar Motion. Uses IAU 2000A nutation model.

    Args:
      tta (float): Terrestrial Time as a 2-part Julian Date (Part a).
      ttb (float): Terrestrial Time as a 2-part Julian Date (Part b).
      UTa (float): UT1 as a 2-part Julian Date (Part a).
      UTb (float): UT1 as a 2-part Julian Date (Part b).
      xp  (float): x-coordinate of the pole (radians).
      yp  (float): y-coordinate of the pole (radians).

    Returns:
      (Numpy Array):

         (3x3) celestial-to-terrestrial matrix


    """
    cdef double rc2t[3][3]  #initialise C array

    iauC2t00a(tta, ttb, uta, utb, xp, yp, rc2t)     #perform sofa routine

    return np.array(rc2t)   #return the array as a numpy object

