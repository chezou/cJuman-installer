all:
#	swig -Wall -python -shadow -I/usr/local/include cJuman.i
	python setup.py build_ext --inplace

.PHONY: clean
clean:
#	rm -rf cJuman_wrap.c cJuman.py _cJuman.so cJuman.pyc
	rm -rf _cJuman.so build
install:
	python setup.py install