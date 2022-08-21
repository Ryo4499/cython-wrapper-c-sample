SRC_DIR = src/

default: hello*.so

hello*.so: setup.py
	python3 setup.py build_ext --inplace && rm -Rf build

clean:
	rm *.so && rm $(SRC_DIR)*.c
