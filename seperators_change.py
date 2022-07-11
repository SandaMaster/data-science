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

# with open('gtlog.csv', 'r', encoding='utf-8') as file:
#     xml = file.read()
#
#     buba = xml.split('\n')
#     lista_linijek = []
#     for i in buba:
#         splited = i.split(', ')
#         linijka = []
#         for x in splited:
#             linijka.append(x.replace(',', '.'))
#         lista_linijek.append(','.join(linijka))
#
#     print(lista_linijek)
#
# df = pd.DataFrame(lista_linijek)
# df.to_csv('gtlog.csv', index = False, header=0)
    #
    # splited_xml2 = joined_xml1.split(",")
    # joined_xml2 = ".".join(splited_xml2)
    #
    # splited_xml3 = joined_xml2.split(";")
    # joined_xml3 = ",".join(splited_xml3)
    #
    # print(joined_xml3)
    #




# header = splited_xml3[0]
# data = splited_xml3[1:]
# col_names = header.split('.')
# header = ','.join(col_names)
# chunk_len = len(col_names)
#
#
# def grouper(n, iterable, fillvalue=None):
#     "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
#     args = [iter(iterable)] * n
#     return zip_longest(fillvalue=fillvalue, *args)
#
#
# for row in grouper(chunk_len, data):
#     print(row)
