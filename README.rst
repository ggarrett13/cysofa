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

.. image:: https://github.com/poliastro/poliastro/raw/master/docs/source/examples/molniya.png
   :align: center

Documentation
=============


Complete documentation, including a user guide and an API reference, can be read on
the wonderful `Read the Docs`_.

https://docs.poliastro.space/

.. _`Read the Docs`: https://readthedocs.org/

Examples
========

.. |mybinder| image:: https://img.shields.io/badge/launch-binder-e66581.svg?style=flat-square
   :target: https://beta.mybinder.org/v2/gh/poliastro/poliastro/master?filepath=index.ipynb


|mybinder|

In the examples directory you can find several Jupyter notebooks with specific
applications of poliastro. You can launch a cloud Jupyter server using `binder`_ to edit
the notebooks without installing anything. Try it out!

https://beta.mybinder.org/v2/gh/poliastro/poliastro/master?filepath=index.ipynb

.. _binder: https://beta.mybinder.org/

Requirements
============

poliastro requires the following Python packages:

* NumPy, for basic numerical routines
* Astropy, for physical units and time handling
* numba (optional), for accelerating the code
* jplephem, for the planetary ephemerides using SPICE kernels
* matplotlib, for orbit plotting
* plotly, for 2D and 3D interactive orbit plotting
* SciPy, for root finding and numerical propagation

poliastro is usually tested on Linux, Windows and OS X on Python
3.5, 3.6 and 3.7 against latest NumPy.

==============  ============  ===================
Platform        Site          Status
==============  ============  ===================
Linux           CircleCI      |circleci|
OS X            Travis CI     |travisci|
Windows x64     Appveyor      |appveyor|
==============  ============  ===================

Installation
============

The easiest and fastest way to get the package up and running is to
install poliastro using `conda <http://conda.io>`_::

  $ conda install poliastro --channel conda-forge

Please check out the `documentation for alternative installation methods`_.

.. _`documentation for alternative installation methods`: https://docs.poliastro.space/en/latest/getting_started.html#alternative-installation-methods

Testing
=======

|codecov|

If installed correctly, the tests can be run using pytest::

  $ python -c "import poliastro.testing; poliastro.testing.test()"
  Running unit tests for poliastro
  [...]
  OK
  $ 

Problems
========

If the installation fails or you find something that doesn't work as expected,
please open an issue in the `issue tracker`_.

.. _`issue tracker`: https://github.com/poliastro/poliastro/issues

Contributing
============

.. image:: https://img.shields.io/waffle/label/poliastro/poliastro/1%20-%20Ready.svg?style=flat-square
   :target: https://waffle.io/poliastro/poliastro
   :alt: 'Stories in Ready'

poliastro is a community project, hence all contributions are more than
welcome! For more information, head to `CONTRIBUTING.rst`_.

.. _`CONTRIBUTING.rst`: https://github.com/poliastro/poliastro/blob/master/CONTRIBUTING.rst

Support
=======

|mailing|

Release announcements and general discussion take place on our `mailing list`_.
Feel free to join!

.. _`mailing list`: https://groups.io/g/poliastro-dev

https://groups.io/g/poliastro-dev

Citing
======

If you use poliastro on your project, please
`drop me a line <mailto:juanlu001@gmail.com>`_.

You can also use the DOI to cite it in your publications. This is the latest
one:

|doi|

And this is an example citation format::

 Juan Luis Cano Rodríguez et al.. (2015). poliastro: poliastro 0.4.0. Zenodo. 10.5281/zenodo.17462

License
=======

|license|

poliastro is released under the MIT license, hence allowing commercial
use of the library. Please refer to the COPYING file.

FAQ
===

What's up with the name?
------------------------

poliastro comes from Polimi, which is the shortened name of the Politecnico di
Milano, the Italian university where I was studying while writing this
software. It's my tiny tribute to a place I came to love. *Grazie mille!*

Can I do <insert awesome thing> with poliastro?
-----------------------------------------------

poliastro is focused on interplanetary applications. This has two consequences:

* It tries to be more general than other Flight Dynamics core libraries more
  focused on Earth satellites (see `Related software`_ for a brief list),
  allowing the algorithms to work also for orbits around non-Earth bodies.
* It leaves out certain features that would be too Earth-specific, such as
  TLE reading, SGP4 propagation, groundtrack plotting and others.

.. _`Related software`: https://docs.poliastro.space/en/latest/about.html#related-software

What's the future of the project?
---------------------------------

poliastro is actively maintained and receiving an influx of new contributors
thanks to the generous sponsorship of Google and the European Space Agency.
The best way to get an idea of the roadmap is to see the `Milestones`_ of
the project.

.. _`Milestones`: https://github.com/poliastro/poliastro/milestones
