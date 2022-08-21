from setuptools import setup, Extension
from Cython.Build import cythonize

SRC_DIR = "./src/"
LIB_DIR = "./lib/"

examples_extension = Extension(
    name="hello",
    sources=[SRC_DIR+"hello.pyx",LIB_DIR+"hello.c"],
    include_dirs=["lib"]
)
setup(
    name="hello",
    ext_modules=cythonize([examples_extension],language_level="3")
)
