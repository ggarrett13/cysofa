#!/usr/bin/env python
import os
from setuptools import setup, find_packages, findall
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

#############################################
# Create extensions from .pyx files
SOFALIB = "./src/cysofa/cypyx/cylib/lib"
SOFAINCLUDE = "./src/cysofa/cypyx/cylib/include"
PYXLOC = "./src/cysofa/cypyx/"
NAMESTRT = "src.cysofa.cypyx.py"

# For iauAnp, iauPfw06, iauc2t00a, iauPn00a, iauGd2gc
IAUNAMES = ["anp", "Pfw06", "C2t00a", "Pn00a", "Gd2gc"]
EXTENSIONS = [
    Extension(
        name="py" + IAUNAME,
        sources=[PYXLOC + "py" + IAUNAME + ".pyx"],
        libraries=["sofa_c"],
        library_dirs=[SOFALIB],
        include_dirs=[SOFAINCLUDE]
    ) for IAUNAME in IAUNAMES
]

############################################
# get version from __init__ file and perform setup
version = {}
with open(os.path.join("src", "cysofa", "__init__.py")) as fp:
    exec(fp.read(), version)

ext_modules = cythonize(EXTENSIONS, compiler_directives={'embedsignature': True})
# for e in ext_modules:
#     e.cython_directives = {"embedsignature": True}
#
# print(ext_modules[0].cython_directives)

# setup(
#     name="cysofa",
#     version=version['__version__'],
#     description="Python wrapper for sofa C library",
#     author="Matthew Turnock",
#     author_email="matthew.turnock1@gmail.com",
#     url="",
#     download_url="",
#     license="MIT",
#     keywords=[
#         "word", "engineering"
#     ],
#     python_requires=">=3.6",
#     install_requires=[
#         "numpy",
#         "cython>=0.29.1"
#     ],
#     extras_require={
#         'dev': [
#             "sphinx"
#         ]
#     },
#     packages=[find_packages('src')],
#     package_dir={'': 'src'},
#     # entry_points={
#     #     'console_scripts': [
#     #         'poliastro = poliastro.cli:main'
#     #     ]
#     # },
#     classifiers=[
#         "Development Status :: 4 - Beta",
#         "Intended Audience :: Education",
#         "Intended Audience :: Science/Research",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: Linux",
#         "Programming Language :: Python",
#         "Programming Language :: Python :: 3",
#         "Programming Language :: Python :: 3.5",
#         "Programming Language :: Python :: 3.6",
#         "Programming Language :: Python :: Implementation :: Cython",
#         "Topic :: Scientific/Engineering",
#         "Topic :: Scientific/Engineering :: Physics",
#         "Topic :: Scientific/Engineering :: Astronomy",
#     ],
#     long_description=open('README.rst', encoding='utf-8').read(),
#     include_package_data=True,
#     # ext_modules=cythonize([anp_extension, Pfw06_extension, C2t00a_extension, Pn00a_extension, Gd2gc_extension]),
#     zip_safe=False,
#     ext_modules=ext_modules,
# )


setup(
    name="cysofa",
    version=version['__version__'],
    description="Python wrapper for sofa C library",
    author="Matthew Turnock",
    author_email="matthew.turnock1@gmail.com",
    url="",
    download_url="",
    license="MIT",
    keywords=[
        "word", "engineering"
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "cython>=0.29.1",
        "numpydoc",
        "sphinx_rtd_theme"
    ],
    extras_require={
        'dev': [
            "sphinx"
        ]
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # entry_points={
    #     'console_scripts': [
    #         'poliastro = poliastro.cli:main'
    #     ]
    # },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: Cython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    long_description=open('README.rst', encoding='utf-8').read(),
    include_package_data=True,
    zip_safe=False,
    ext_modules=ext_modules,
)
