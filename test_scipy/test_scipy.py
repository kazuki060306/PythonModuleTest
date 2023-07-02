import numpy
from testmodule import _test_linear_filter

a = numpy.array([6.0, 2.0, 2.0, 3.0, 5.0, 4], dtype=float)
b = numpy.array([6.0, 8.0, 6.0, 2.0, 7.0, 8], dtype=float)
x = numpy.array([7.0, 3.0, 9.0, 7.0, 9.0, 7.0, 8.0, 3.0, 8.0, 6.0, 6.0, 5.0, 8.0, 5.0, 6.0, 8.0, 3.0, 8], dtype=float)
v = numpy.array([6.0, 2.0, 3.0, 5.0, 4], dtype=float)

print(_test_linear_filter(b, a, x, -1, v))
#test(lambda d: [fast_tanh(x) for x in d], '[fast_tanh(x) for x in d] (CPython C++ extension)')

#from superfastcode2 import fast_tanh2
#test(lambda d: [fast_tanh2(x) for x in d], '[fast_tanh2(x) for x in d] (PyBind11 C++ extension)')
