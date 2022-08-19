from setuptools import setup, Extension
from Cython.Build import cythonize

SRC_DIR = "./src/"
LIB_DIR = "./lib/"

examples_extension = Extension(
    name="pyexamples",
    sources=[SRC_DIR+"pyexamples.pyx",LIB_DIR+"main.c"],
    include_dirs=["lib"]
)
setup(
    name="pyexamples",
    ext_modules=cythonize([examples_extension],language_level="3")
)
