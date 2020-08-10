import numpy

# Slicing refers to extracting a portion of existing array.
#
# This can be achieved with a slice object.
#
# A slice object is of the form start:end:step. All three are optional.
#
# Having only a single number inside square brackets refer to start index.

x = numpy.array([5, 10, 15, 20, 25, 30, 35])
# print(x[1])  # Indexing
# print(x[1:6]) # Slicing
# print(x[1:6:3]) # Slicing

# Two slice objects, one for each dimension, are required to slice a 2-D array.
y = numpy.array([[0, 1, 2],
              [3, 4, 5]])
# print(y[1:2, 1:3])
# print(y[1])
# print(y[:, 1])

# for loop can be used to iterate over every dimension of array
x1 = numpy.array([[-1, 1], [-2, 2]])
# for row in x1:
#     print('Row :',row)

# nditer method of numpy creates an iterator, which enable accessing each element one after the other.
x2 = numpy.array([[0,1], [2, 3]])
# for a in numpy.nditer(x2):
#     print(a)

x3 = numpy.arange(30).reshape(3,5,2)
# print(x3)
# print(x3[1][::2][1])

x4 = numpy.arange(30).reshape(3,5,2)
# print(x4)
# print(x4[-1, 2:-1, -1])
# print(x4[-1,2:-1])

x5 = numpy.array([[1, 2], [3, 4], [5, 6]])
# print(x5[[0, 1, 2], [0, 1, 1]])





