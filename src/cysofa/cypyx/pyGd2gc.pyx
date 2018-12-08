STUFF = 'hi'
import numpy as np

cdef extern from "sofa.h":
    int iauGd2gc ( int n, double elong, double phi, double height,
                   double xyz[3])

def py_iauGd2gc(int n, double elong, double phi, double height, return_status=False):
    """Wrapper for iauGd2gc module (`SOFA Documentation <http://www.iausofa.org/current_C.html>`_.). Transform geodetic coordinates to geocentric using the specified reference ellipsoid.

    Args:
      n (int): Ellipsoid identifier.
      elong (float): Longitude with East positive (radians).
      phi (float): Geodetic latitude (radians).
      height (float): Geodetic height above ellipsoid (m).
      return_status  (bool, optional): Choose whether or not to return the SOFA validation status.

    Returns:
      (Numpy Array or tuple):

         * If return_status = False --> xyz -- (1x3) geocentric vector (m)
         * If return_status = True --> The tuple (xyz, status).

    .. note::
       The values of status are:
          * 0 = OK
          * -1 = illegal identifier
          * -2 = illegal case

    """
    #Initialise output matrix
    cdef double xyz[3]

    #Do the C routine, returning the status
    status = iauGd2gc(n, elong, phi, height, xyz)

    #return tuple of xyz array and the status
    xyz = np.array(xyz)

    if return_status:
        return xyz, status
    else:
        return xyz