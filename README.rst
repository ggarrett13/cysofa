.. poliastro




:Name: A very good python package
:Website:
:Author: Matthew Turnock
:Version: 0.0



This python package is amAZing, so much winning you wouldn't believe.

.. code-block:: python

    from poliastro.examples import molniya
    from poliastro.plotting import plot
    
    plot(molniya)

.. image:: https://github.com/MattTurnock/package_template/blob/master/docs/examples/trumpy.jpg
   :align: center

Documentation
=============


Complete documentation can be found elsewhere

Examples
========



If you want examples you make em yourself

Requirements
============

this package requires the following Python packages:

* NumPy, for basic numerical routines
* Astropy, for physical units and time handling
* numba (optional), for accelerating the code
* jplephem, for the planetary ephemerides using SPICE kernels
* matplotlib, for orbit plotting
* plotly, for 2D and 3D interactive orbit plotting
* SciPy, for root finding and numerical propagation

this package is usually tested on Linux

==============  ============  ===================
Platform        Site          Status
==============  ============  ===================
Linux           CircleCI      deD

==============  ============  ===================

Installation
============

Some information on installation goes here

Testing
=======

Did you make unit tests? I didn't think so::

  $ python -c "import poliastro.testing; poliastro.testing.test()"
  Running unit tests for poliastro
  [...]
  OK
  $ 

License
=======

this package is released under the MIT license, hence allowing commercial
use of the library. Please refer to the LICENSE file.

FAQ
===

What's up with the name?
------------------------

I didnt make one yet
