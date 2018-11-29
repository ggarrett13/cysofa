#!/usr/bin/env python
import os
from setuptools import setup, find_packages


# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open(os.path.join("src", "package_name", "__init__.py")) as fp:
    exec(fp.read(), version)


# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="cysofa",
    version=version['__version__'],
    description="Python package for something",
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
        "astropy>=3.0,<4.*",
        "matplotlib<3.0.1",
        "jplephem",
        "scipy",
        "beautifulsoup4>=4.5.3",
        "requests",
        "pandas",
        "plotly>=3.0,<4.*",
        "astroquery>=0.3.8",
    ],
    extras_require={
        ':implementation_name=="cpython"': "numba>=0.39",
        'dev': [
            "coverage",
            "pytest",
            "pytest-cov<2.6.0",
            "pycodestyle",
            "sphinx",
            # "sphinx_rtd_theme",  # Use https://github.com/Juanlu001/sphinx_rtd_theme/archive/js-head.zip
            "nbconvert<5.4",
            "nbsphinx",
            "ipython>=5.0",
            "jupyter-client",
            "ipykernel",
            "ipywidgets",
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
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    long_description=open('README.rst', encoding='utf-8').read(),
    include_package_data=True,
    zip_safe=False,
)
