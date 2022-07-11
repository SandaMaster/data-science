import os
import random
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
from itertools import zip_longest


note = r"C:\Users\wjqbfc\Desktop\list.txt"
path = r"Z:\Synthetic movies"

List2 =[]
List = []
lists = []
source = []
all_fill_STD =[]

for roots, folders, files in os.walk(path):
    for folder in folders:
        if folder.endswith("beta"):
            List.append(folder)

    for folder1 in folders:
        if folder1.endswith("1.1.3"):
            List.append(folder1)


with open(note, 'r', encoding="utf-8") as z:
    dupa = z.read()
    lists.append(dupa)

for i in lists:
    source.append(i.replace("\n", " "))


splited = source[0].split(" ")

for x in splited:
    List2.append(x)

print(len(List))
print(len(List2))

for z in List:
    print(z)
# for a in List:
#     all_fill_STD.append(a)
#
# for b in List2:
#     all_fill_STD.append(b)
#
# print(len(all_fill_STD))
#
# print(set(list(all_fill_STD)))
#
#
# # zip(List,List2)
#
# for a,b in zip(List,List2):
#     print(a,b)
#     all_fill_STD.append(a)
#     all_fill_STD.append(b)

