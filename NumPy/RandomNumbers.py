import numpy


numpy.random.seed(100) # setting seed
x = numpy.random.rand(2) # 2 random numbers between 0 and 1


print(x)

numpy.random.seed(100) # setting seed
y = numpy.random.randint(10, 500, 10) # 3 random integers between 10 and 50

print(y)


# if the seed is same output will always be same
