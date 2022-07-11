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


List_element =[]

def find_all(path):
    for roots, folders, files in os.walk(path):
        for file in files:
            source = os.path.join(roots, file)
            with open(source, 'r', encoding="utf-8") as x:
                for line in x:

                    ingest_index = line.find("ingest")
                    film_index = line.find('a310')
                    film_index2 = line.find('a350')
                    film_index3 = line.find('a3c8')

                    if ingest_index > 0:
                        id = line[ingest_index + 7:ingest_index + 13]
                        if id.isdigit():
                            print(id)
                            List_element.append(id)


                    if film_index > 0:
                        film = line[film_index + 5 :film_index + 100 ]
                        if film.startswith('AP'):
                            print(film)
                            List_element.append(film)

                    if film_index2 > 0:
                        film2 = line[film_index2 + 5 :film_index2 + 100 ]
                        if film2.startswith('AP'):
                            print(film2)
                            List_element.append(film2)


                    if film_index3 > 0:
                        film3 = line[film_index3 + 5 :film_index3 + 100 ]
                        if film3.startswith('AP'):
                            print(film3)
                            List_element.append(film3)


path = r"C:\Users\wjqbfc\Desktop\gmdm"
find_all(path)

# splited_line = line.split('/')

# for i in splited_line:
#     if i.endswith('.csv'):
#         print(i)
