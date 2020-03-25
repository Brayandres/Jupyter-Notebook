import numpy as np
import matplotlib.pyplot as plt
from sys import stdin
from Matrx import *

a = 1/math.sqrt(12)
b = 1/math.sqrt(6)
c = -1/math.sqrt(12)
d = -1/math.sqrt(6)

m = Matrx([Vector([Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((c, a)), Cartesian((d, b)), Cartesian((0, 0)), Cartesian((1, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((c, c)), Cartesian((d, d)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((1, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((0, 0)), Cartesian((d, b)), Cartesian((b, d)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((1, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((c, c)), Cartesian((0, 0)), Cartesian((d, d)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((1, 0)), Cartesian((0, 0))]),
           Vector([Cartesian((c, a)), Cartesian((0, 0)), Cartesian((b, d)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((1, 0))])])

p = 1/math.sqrt(2)

v = Vector([Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((c, a)), Cartesian((c, c)), Cartesian((0, 0)), Cartesian((c, c)), Cartesian((c, a))])

clicks = 2
for i in range(clicks):
    v = m.actOnVect(v)

labels = ["Pto.0", "Pto.1", "Pto.2", "Pto.3", "Pto.4", "Pto.5", "Pto.6", "Pto.7"]
estado = [v.numbers[0].element_1,
          v.numbers[1].element_1,
          v.numbers[2].element_1,
          v.numbers[3].element_1,
          v.numbers[4].element_1,
          v.numbers[5].element_1,
          v.numbers[6].element_1,
          v.numbers[7].element_1]
index = np.arange(len(labels))
plt.bar(index, estado)
plt.xlabel("Estado")
plt.ylabel("Valor")
plt.xticks(index, labels, rotation = 75)
plt.title("Evolución Dinámica del sistema luego de "+str(clicks)+" click(s) de tiempo:")
plt.show()
