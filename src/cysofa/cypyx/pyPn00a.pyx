STUFF = 'hi'
import numpy as np

cdef extern from "sofa.h":
    void iauPn00a(double date1, double date2,
              double *dpsi, double *deps, double *epsa,
              double rb[3][3], double rp[3][3], double rbp[3][3],
              double rn[3][3], double rbpn[3][3])

def py_iauPn00a(double date1, double date2):
    """Wrapper for iauPn00a module (`SOFA Documentation <http://www.iausofa.org/current_C.html>`_.). Given the date, returns various variables from the IAU 2000A precession-nutation model.

    Args:
      date1 (float): Terrestrial Time as a 2-part Julian Date (Part 1).
      date2 (float): Terrestrial Time as a 2-part Julian Date (Part 2).

    Returns:
      (tuple):

         Length 7 tuple containing:
            * **dpsi** -- :math:`\mathbf{\psi}` component of IAU 2000A nutation model (radians).
            * **deps** -- :math:`\mathbf{\epsilon}` component of IAU 2000A nutation model (radians).
            * **epsa** -- Mean obliquity, consistent with IAU 2000 precession.
            * **rb** -- (3x3) Numpy Array containing frame bias matrix. The matrix transforms vectors from GCRS to J2000.0 mean equator and equinox by applying frame bias.
            * **rp** -- (3x3) Numpy Array containing precession matrix. The matrix transforms vectors from J2000.0 mean equator and equinox to mean equator and equinox of date by applying precession.
            * **rbp** -- (3x3) Numpy Array containing bias-precession matrix. The matrix transforms vectors from GCRS to mean equator and equinox of date by applying frame bias then precession.  It is the product rp x rb.
            * **rn** -- (3x3) Numpy Array containing nutation matrix. The matrix transforms vectors from mean equator and equinox of date to true equator and equinox of date by applying the nutation (luni-solar + planetary).
            * **rbpn** -- (3x3) Numpy Array containing GCRS-to-true matrix. The matrix transforms vectors from GCRS to true equator and equinox of date.  It is the product rn x rbp, applying frame bias, precession and nutation in that order.

    .. note::
       If only the transformation from GCRS to true is required, then take the **rbpn** output.

    """
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