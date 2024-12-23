# -*- coding: utf-8 -*-
"""ЛАБА6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1txRFpvaSREzslBzNfteXOQfe3rkSbgI0
"""

def f_to_k(temp_f):
  temp_k =(temp_f-32)/1.8+273.15
  return temp_k
temp3_f=[-270, 20, 212]
for temp_f in temp3_f:
    temp_k=f_to_k(temp_f)
    print(f"{temp_f}°F ={temp_k:.2f} K")

!pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
data = np.random.randn(1000)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color="skyblue", edgecolor="black")
plt.title("Гистограмма случайных данных")
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.grid(axis="y", alpha=0.75)
plt.show()
x = np.random.rand(100)
y = np.random.rand(100)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="purple", alpha=0.6)
plt.title("Скаттер-график")
plt.xlabel("Значение X")
plt.ylabel("Значение Y")
plt.grid()
plt.show()
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(8, 6))
plt.fill_between(x, y1, color="skyblue", alpha=0.4, label="sin(x)")
plt.fill_between(x, y2, color="orange", alpha=0.4, label="cos(x)")
plt.title("График с областями")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

import math
def NOD(a,b):
    while b:
        a,b=b,a%b
    return a
enum=math.e
print(f"Число Эйлера:{enum}")
pi=math.pi
print(f"Число Пи:{pi}")
nan=math.nan
print(f"NaN:{nan}")
pornum=5
fact=math.factorial(pornum)
print(f"Факториал числа {pornum}: {fact}")
num1=pornum
num2=512
NOD_=NOD(num1,num2)
print(f"НОД чисел {num1} и {num2}: {NOD_}")

import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(6,6))
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.axis('off')
num_circles=8
radius=5
for i in range(num_circles):
    angle=i*(360/num_circles)
    x=radius*np.cos(np.radians(angle))
    y=radius*np.sin(np.radians(angle))
    circle=plt.Circle((x,y),radius, color=plt.cm.viridis(i/num_circles), alpha=0.6, edgecolor="black", linewidth=1)
    ax.add_patch(circle)
plt.show()