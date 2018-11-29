LIB_DIR = cypyx/cylib/lib
PYX_DIR = cypyx



default: py_sofa

py_sofa: setup.py
	python3 setup.py build_ext --build-lib ./cypyx


clean:
	rm ./cypyx/*.so

#Use tidy to get rid of non-required .c files that are generated
tidy:
	rm $(PYX_DIR)/*.c && rm -rf build