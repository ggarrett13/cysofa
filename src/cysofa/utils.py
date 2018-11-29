from cypyx import pyanp, pyC2t00a, pyGd2gc, pyPfw06, pyPn00a
import numpy as np
def pAnp(x):
    """This function does something.

    :param name: The name to use.
    :type name: str.
    :param state: Current state to be in.
    :type state: bool.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError

    """
    return pyanp.py_iauAnp(x)



def pC2t00a(tt1, tt2, ut1, ut2, xp,yp):
    """This function does something.

    :param name: The name to use.
    :type name: str.
    :param state: Current state to be in.
    :type state: bool.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError

    """
    return pyC2t00a.py_iauC2t00a(tt1, tt2, ut1, ut2, xp, yp)


def pGd2gc(n, elong, phi, height):
    """This function does something.

    :param name: The name to use.
    :type name: str.
    :param state: Current state to be in.
    :type state: bool.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError

    """

    return pyGd2gc.py_iauGd2gc(n, elong, phi, height)

def pPfw06(tt1, tt2):
    """This function does something.

    :param tt1: Terrestrial Time (part 1 of 2-part Julian date)
    :type name: float
    :param tt2: Terrestrial Time (part 2 of 2-part Julian date)
    :type state: float
    :returns:  tuple -- tuple of length 4 containing Fukushima-Williams angles (gamb, phib, psib, epsa)

    """
    return pyPfw06.py_iauPfw06(tt1, tt2)



def pPn00a(tt1, tt2):
    """This function does something.

    :param tt1: Terrestrial Time (part 1 of 2-part Julian date)
    :type name: float
    :param tt2: Terrestrial Time (part 2 of 2-part Julian date)
    :type state: float
    :returns:  tuple -- tuple of length 4 containing Fukushima-Williams angles (gamb, phib, psib, epsa)

    """
    return pyPn00a.py_iauPn00a(tt1, tt2)
