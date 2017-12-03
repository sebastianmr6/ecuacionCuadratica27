#-*- coding: utf-8 -*-

import math
class ecuacionCuadratica():


    a = input("Ingrese valor A= ")
    b = input("Ingrese valor B= ")
    c = input("Ingrese valor C= ")
    if a == 0:
        print u"error, división por 0"
    elif b ** 2 - 4 * a * c < 0:
        print u"no tiene solución en los reales"
    else:
        x1 = (- b + math.sqrt( b**2 - 4 * a * c ))/( 2 * a )
        x2 = (- b - math.sqrt( b**2 - 4 * a * c ))/( 2 * a )
        print "El valor de x1 es = " + str(x1)
        print "El valor de x1 es = " + str(x1)

