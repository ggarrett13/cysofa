#STUFF = "Hi"
#DEFINITION FOR THE ANP
cdef extern from "sofa.h":
    double iauAnp(double a)

def py_iauAnp(double x):
    """Wrapper for iauAnp module (`SOFA Documentation <http://www.iausofa.org/current_C.html>`_.). Normalise angle into the range 0 <= x < 2pi.

    Args:
      x (float): Angle (radians)

    Returns:
      (float):

         Normalised angle

    """

    return iauAnp(x)