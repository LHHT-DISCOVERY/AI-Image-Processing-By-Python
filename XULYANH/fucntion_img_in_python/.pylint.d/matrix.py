import numpy

a = [
    [0, 1, 0, 0, 0, 3],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
a = numpy.array(a)
print(numpy.sum(a))
print(a)

print(a[0,5])
