import os
import random
import runpy
from pathlib import Path
import os
import glob
import numpy as np
import pandas
import pandas as pd
import csv
import shutil
import xmltodict
import pprint

double_x = []
index_x = []
list_x = []
list_y = []
sum_product = []


def bogdan_boner(path):
    for roots, folders, files in os.walk(path):

        for file in files:
            if file.startswith("lista_x"):
                source = os.path.join(roots, file)

                with open(source, 'r', encoding="utf-8") as x:
                    destiny = x.read()
                    elements = destiny.split(" ")
                    for point in elements:
                        mark = float(point)
                        list_x.append(mark)

            if file.startswith("lista_y"):
                source = os.path.join(roots, file)

                with open(source, 'r', encoding="utf-8") as y:
                    destiny = y.read()
                    elements = destiny.split(" ")
                    for point in elements:
                        mark = float(point)
                        list_y.append(mark)


path = r'C:\Users\Grzegorz Mróz\Desktop'
bogdan_boner(path)


def marcinek():
    global base_a, base_b
    for i in list_x:
        actual_index_x = list_x.index(i)
        index_x.append(actual_index_x + 1)

    for j in list_x:
        double = j ** 2
        double_x.append(double)

    sum_list_x = sum(list_x)
    sum_list_y = sum(list_y)
    double_sum_list_x = sum(double_x)

    particular_elements = zip(list_x, list_y)

    for a, b in particular_elements:
        sum_product.append(a * b)

    all_elements = zip(list_x, list_y, index_x, sum_product)

    for x, y, n, s in all_elements:
        base_a = (sum_list_x * sum_list_y - n * s) / ((sum_list_x ** 2) - n * double_sum_list_x)
        base_b = (sum_list_x * s - double_sum_list_x * sum_list_y) / (sum_list_x ** 2 - n * double_sum_list_x)
    print(base_a, base_b)


marcinek()

