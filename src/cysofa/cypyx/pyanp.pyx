#STUFF = "Hi"
#DEFINITION FOR THE ANP
cdef extern from "sofa.h":
    double iauAnp(double a)

def py_iauAnp(double x):
    """
    py_iauAnp(double x)
    soccers
    """
    return iauAnp(x)