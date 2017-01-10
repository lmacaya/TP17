# -*- coding: UTF-8 -*-
from matplotlib.pyplot import *

x = [5, 20, 40, 60, 80]
y = [2.6, 5.5, 7, 12.5, 11.9]

plt.plot(x,y, marker="o", markersize=5, color="green", label="Datos experimentales")
plt.title("Voltaje versus Frecuencia")
plt.xlabel("Frecuencia $f$ [Hertz]")
plt.ylabel("Voltaje $V$ [Volt]")
plt.legend(loc=2) # esquina superior izquierda
plt.savefig("g1.pdf")