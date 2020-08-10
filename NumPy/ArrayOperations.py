import numpy

# sum rows vertically axis=0, horizontally axis=1

# arr.sum(axis=0)

x = numpy.arange(4)
y = numpy.arange(4)
# print(x == y)

x1 = numpy.random.randint(1,6,(2,3))
# print(numpy.square(x1))
# print(x1 + 5)

x2 = numpy.random.randint(-30,30,(5,6))
# print(x2)
# print(x2.sum(axis=0))
# print(x2.sum(axis=1))

# array with normal mean and standard deviation
x3 = numpy.random.normal(10,2,(50,))
# print(x3)
# print(x3.mean())
# print(x3.std())
# print(x3.var())
