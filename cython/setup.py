
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name="Hello",
    # ext_modules=[
    #     Extension('utils', ["hello/utils.pyx", ]),
    #     Extension('hello2', ["hello2.py", ]),
    # ],
    ext_modules=cythonize(["utils.pyx", "hello2.py"]),
)
