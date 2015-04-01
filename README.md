cJuman installer
==========================
2011/09/25 chezou

This is cJuman installer.
cJuman is Python wrapper of JUMAN using swig.

Juman

http://nlp.ist.i.kyoto-u.ac.jp/index.php?%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0JUMAN

cJuman

http://app-dist.khlog.net/software/python-cjuman/

Install Dependencies
--------------------
You need install JUMAN before build.

To install cJuman, run
--------------------

   % python setup.py build

   % sudo python setup.py install

To create wheel 
--------------------

To create whl archive, the setuptools and wheel are needed.

   % python setup.py bdist_wheel

License
--------------------
MIT License
