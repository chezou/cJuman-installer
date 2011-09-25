#!/usr/bin/env python

from distutils.core import setup, Extension

ext_module = Extension('_cJuman',
                       sources=['cJuman_wrap.c'],
                       libraries=["juman"],
                       )

setup(name='cJuman',
      version='0.1',
      author='chezou',
      author_email='chezou@gmail.com',
      ext_modules=[ext_module],
      py_modules=['cJuman'],
      )
