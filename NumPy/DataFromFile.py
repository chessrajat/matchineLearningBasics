from io import StringIO
import numpy

# loadtxt is used to read data from a text file or any input data stream.

x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')

d = numpy.loadtxt(x, delimiter=' ')

print(d)

print(d.ndim, d.shape)

