import numpy

speed = [32,111,138,28,59,77,97]

x1 = numpy.var(speed)
x2 = numpy.std(speed)

print(x1, x2**2)
