from setuptools import setup, Extension

sfc_module = Extension('testmodule', sources = ['module.cpp'], include_dirs = ['C:/Users/kazuk/AppData/Local/Programs/Python/Python311/Lib/site-packages/numpy/core/include'])

setup(
    name='testmodule',
    version='1.0',
    description='Python Package with testmodule C++ extension',
    ext_modules=[sfc_module]
)