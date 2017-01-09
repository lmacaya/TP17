# -*- coding: UTF-8 -*-

print("Resolveremos la ecuacion a * x ** 2 + b * x + c = 0 y (- b +- ( b ** 2 - 4 * a * c) ** 0.5) / 2 * a")
a=float(raw_input("Valor de a = "))
b=float(raw_input("Valor de b = "))
c=float(raw_input("Valor de c = "))
print("La ecuacion 1 a resolver es: + "+ str(a) +" x ** 2 + ("+str(b)+") x + ("+str(c)+")")
print("La ecuacion 2 a resolver es: - ( " + str(b) + " +- ( "+ str(b) +" ** 2 - 4 * " + str(a*c) + " ) ** 0.5 ) / 2 * "+ str(a))

solucion_1 = "- ( " + str(b) + " + ( "+ str(b) +" ** 2 - 4 * " + str(ac) + " ) ** 0.5 ) / 2 * "+ str(a)
solucion_2 = "- ( " + str(b) + " - ( "+ str(b) +" ** 2 - 4 * " + str(ac) + " ) ** 0.5 ) / 2 * "+ str(a)
print("Solución 1: " + solucion_1)
print("Solución 2: " + solucion_2)
   