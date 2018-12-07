#STUFF = "Hi"
#DEFINITION FOR THE ANP
cdef extern from "sofa.h":
    double iauAnp(double a)

def py_iauAnp(double x):
    """ADD DOCUMENTATION HERE"""

    return iauAnp(x)

