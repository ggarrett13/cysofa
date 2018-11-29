from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

SOFALIB = "cypyx/cylib/lib"
SOFAINCLUDE = "cypyx/cylib/include"
PYXLOC = "cypyx/"

#For iauAnp
IAUNAME = "anp"
anp_extension = Extension(
    name="py" + IAUNAME,
    sources=[PYXLOC + "py" + IAUNAME + ".pyx"],
    libraries=["sofa_c"],
    library_dirs=[SOFALIB],
    include_dirs=[SOFAINCLUDE]
)
setup(
    name="py" + IAUNAME,
    ext_modules=cythonize([anp_extension])
)

#For iauPfw06
IAUNAME = "Pfw06"
Pfw06_extension = Extension(
    name="py" + IAUNAME,
    sources=[PYXLOC + "py" + IAUNAME + ".pyx"],
    libraries=["sofa_c"],
    library_dirs=[SOFALIB],
    include_dirs=[SOFAINCLUDE]
)
setup(
    name="py" + IAUNAME,
    ext_modules=cythonize([Pfw06_extension, anp_extension])
)

#For iauc2t00a
IAUNAME = "C2t00a"
C2t00a_extension = Extension(
    name="py" + IAUNAME,
    sources=[PYXLOC + "py" + IAUNAME + ".pyx"],
    libraries=["sofa_c"],
    library_dirs=[SOFALIB],
    include_dirs=[SOFAINCLUDE]
)
setup(
    name="py" + IAUNAME,
    ext_modules=cythonize([C2t00a_extension])
)

#For iauPn00a
IAUNAME = "Pn00a"
Pn00a_extension = Extension(
    name="py" + IAUNAME,
    sources=[PYXLOC + "py" + IAUNAME + ".pyx"],
    libraries=["sofa_c"],
    library_dirs=[SOFALIB],
    include_dirs=[SOFAINCLUDE]
)
setup(
    name="py" + IAUNAME,
    ext_modules=cythonize([Pn00a_extension])
)

#For iauGd2gc
IAUNAME = "Gd2gc"
Gd2gc_extension = Extension(
    name="py" + IAUNAME,
    sources=[PYXLOC + "py" + IAUNAME + ".pyx"],
    libraries=["sofa_c"],
    library_dirs=[SOFALIB],
    include_dirs=[SOFAINCLUDE]
)
setup(
    name="py" + IAUNAME,
    ext_modules=cythonize([Gd2gc_extension])
)