LIB_DIR = lib

default: pyexamples

pyexamples: setup.py
	python3 setup.py build_ext --inplace && rm -f pyexamples.c && rm -Rf build

clean:
	rm *.so
