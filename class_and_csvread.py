import random
from pathlib import Path
import os
import glob
import math
import numpy as np
import pandas
import pandas as pd
import csv
import shutil
import xmltodict
import pprint

# path = r"C:\Users\wjqbfc\Desktop\Push mdm\csvki.txt"
# with open(path, 'r') as csvfile:
#     measure = [l for l in csvfile.readlines()]
#     measure_list = list(set(measure))
#     for i in measure_list:
#         print(i)

class Figura:

    def obwod(self):
        'liczenie obw'
        return NotImplementedError
    def pole(self):
        'liczenie pola'
        return NotImplementedError
    def przekatna(self):
        'liczenie przek'
        return NotImplementedError

class kolo(Figura):

    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2*math.pi*self.r

    def pole(self):
        return math.pi*self.r**2

o = kolo(4)
print(o.pole())
print(o.obwod())



class prostokat(Figura):

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a*self.b



k = prostokat(3,5)
print(k.pole())
print(k.obwod())




class kwadrat(Figura):

    def __init__(self, a):
        self.a = a

    def pole(self):
        return self.a**2

    def obwod(self):
        return self.a*4

    def przekatna(self):
        return self.a * math.sqrt(2)

l = kwadrat(6)
print(l.pole())
print(l.obwod())
print(l.przekatna())

