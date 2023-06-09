# -*- coding: utf-8 -*-
"""Tarea1_Karol_Salazar

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-1FBl-dzCeWnZaoI5Y2ZaJ7ua2WMagqh

##General
"""

import math
class Vector:
  def __init__(self, coordenada_x, coordenada_y, coordenada_z):
    self.x = coordenada_x
    self.y = coordenada_y
    self.z = coordenada_z
    self.magnitud = (self.x**2 + self.y**2 + self.z**2)**0.5
  def __str__(self):
    respuesta = "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"
    return(respuesta)
  def suma(self, otra):
    respuesta = Vector(self.x+otra.x,self.y+otra.y, self.z+otra.z)
    return(respuesta)
  def escalar(self, otra):
    return(self.x*otra.x+self.y*otra.y)

"""##Parte uno, definir el producto vectorial"""

1# Defino vectores
x_1 = float(input("Ingrese coordenada X1: "))
y_1 = float(input("Ingrese coordenada Y1: "))
z_1 = float(input("Ingrese coordenada Z1: "))

x_2 = float(input("Ingrese coordenada X2: "))
y_2 = float(input("Ingrese coordenada Y2: "))
z_2 = float(input("Ingrese coordenada Z2: "))

vec_1=Vector(x_1, y_1, z_1)
vec_2=Vector(x_2, y_2, z_2)

x_res = (y_1*z_2)-(z_1*y_2)
y_res = ((x_1*z_2)-(z_1*x_2))*(-1)
z_res = (x_1*y_2)-(y_1*x_2)

vector_Resultado=Vector(x_res,y_res,z_res)

print("Vector 1:",vec_1)
print("Vector 2:",vec_2)
print("Suma",vec_1.suma(vec_2))

"""
  vec_1.x -> obtiene la parte X del vector 1
  vec_1.y -> obtiene la parte Y del vector 1
  vec_2.x -> obtiene la parte X del vector 2
  vec_2.y -> obtiene la parte Y del vector 2
"""

print("Producto vectorial",vector_Resultado)

"""##Parte dos, aplicación de física

###la aplicación es de la "ecuación del espejo"

Se desea hallar la distancia a la cuál se reproduce una imagen (q)

Tenemos el valor de la distancia sobre la cuál se encuentra el objeto (p)

Tenemos el valor de la distancia del punto focal (f)
"""

import math
p = float(input("Ingrese la distancia (p): "))
f = float(input("Ingrese la distancia (f): "))

"""
  Fórmula de la ecuación del espejo:
  (1/p) + (1/q) = 1/f
  tenemos que hallar (q) entonces despejamos:
  1/q = (p-f)/(pf)
  q = (p*f)/(p-f)
"""
q = (p*f)/(p-f)

print("La distancia a la cuál se reproduce la imagen (q) es:", q)