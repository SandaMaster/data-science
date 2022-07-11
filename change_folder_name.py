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

#
# def change_name_MAX(file_path):
#      for roots, dirs, files in os.walk(file_path):
#
#         for dir in dirs:
#             if dir.startswith('AP0'):
#                 splited_dirs = dir.split('_')
#
#
#                 software = 'X044'
#                 hardware = 'B'
#
#
#
#
#                 if len(splited_dirs) == 7:
#                     splited_dirs1 = splited_dirs[6].split('#')
#
#                     test_subject = splited_dirs[0]
#                     scenario_id = splited_dirs[3]
#                     date = splited_dirs[4]
#                     software_num = software
#                     hardware_num = hardware
#                     xylon_hash = splited_dirs1[1]
#
#
#
#                 elif len(splited_dirs) == 11:
#                     splited_dirs1 = splited_dirs[10].split('#')
#
#                     test_subject = splited_dirs[0]
#                     scenario_id = splited_dirs[3]
#                     date = splited_dirs[4]
#                     software_num = software
#                     hardware_num = hardware
#                     xylon_hash = splited_dirs1[1]
#
#
#                 elif len(splited_dirs) == 13:
#                     splited_dirs1 = splited_dirs[12].split('#')
#
#                     test_subject = splited_dirs[0]
#                     scenario_id = splited_dirs[3]
#                     date = splited_dirs[4]
#                     software_num = splited_dirs[7]
#                     hardware_num = splited_dirs[8]
#                     xylon_hash = splited_dirs1[1]
#
#
#                 elif len(splited_dirs) == 14:
#                     splited_dirs1 = splited_dirs[13].split('#')
#
#                     test_subject = splited_dirs[0]
#                     scenario_id = splited_dirs[3]
#                     date = splited_dirs[4]
#                     software_num = splited_dirs[7]
#                     hardware_num = splited_dirs[8]
#                     xylon_hash = splited_dirs1[1]
#
#
#
#
#                 else:
#                     print('Unhandled length of dirs')
#
#
#                 new_name = (f'{test_subject}_001_SQ5_{scenario_id}_{date}_MAX_static_{software_num}_{hardware_num}#{xylon_hash}')
#                 print(new_name)
#
#
#             old_name_path = os.path.join(roots, dir)
#             old_name = os.path.basename(dir)
#
#             if os.path.isdir(old_name_path):
#                 new_path = old_name_path.replace(old_name, new_name )
#
#                 if dir != new_name:
#                     os.rename(old_name_path, new_path)
#
#
#
#
#         for file in files:
#             splited_file = file.split('_')
#
#             for element in splited_file:
#
#                 if len(element) == 6 and element.isdigit():
#                     index = splited_file.index(element)
#                     splited_file = splited_file[:index - 3] + splited_file[index + 1:]
#
#             if 'sample' in splited_file:
#                 index = splited_file.index('sample')
#                 splited_file = splited_file[:index] + splited_file[index + 1:]
#
#             if 'X044' not in splited_file:
#                 index = splited_file.index('static')
#                 splited_file.insert(index + 1, 'X044')
#                 splited_file.insert(index + 2, 'B')
#
#             new_file = '_'.join(splited_file)
#             print(new_file)
#
#             splited_new_file = new_file.split('_')
#
#             if 'B' in new_file:
#                 index = splited_new_file.index('B')
#                 splited_new_file = splited_new_file[index: ]
#
#             splited_new_file = '_'.join(splited_new_file[1:])
#             print(splited_new_file)
#
#             source = os.path.join(roots,file)
#             name_file = os.path.basename(file)
#             if os.path.isfile(source):
#                 suf = os.path.basename(roots)
#                 suf = suf.split('#')[0]
#                 suffix = suf + splited_new_file
#                 destiny = source.replace(name_file, suffix)
#                 if file != destiny:
#                     new_source = os.path.join(roots, destiny)
#                     os.rename(source, new_source)
#
#
#
# file_path = r''
# change_name_MAX(file_path)


# ---------X043-----------------

# source_dir = Path(r'')
# for file in source_dir.glob('*'):
# if any([x in file.name for x in ['20211119', '20211122''20211125', '20211126', '20211129', '20211130']]):
#     file.replace(file.with_name(file.name.replace('X044', 'X043')))
# if file.name.startswith('AP024') and '20211201' in file.name:
#     file.replace(file.with_name(file.name.replace('X044', 'X043')))

# for files in file.glob('*'):
#     if any([x in files.name for x in ['20211119', '20211122', '20211125', '20211126', '20211129', '20211130']]):
#         files.replace(files.with_name(files.name.replace('X044', 'X043')))
#     if files.name.startswith('AP024') and '20211201' in files.name:
#         files.replace(files.with_name(files.name.replace('X044', 'X043')))
#
#


# ---------_B_-------------


# p = r''
#
# for roots, dirs, files in os.walk(p):
#     for file in files:
#         source = os.path.join(roots,file)
#         name_file = os.path.basename(file)
#         name_file1 = name_file.split('_B')
#         name = '_B_'.join(name_file1)
#         target_path = os.path.join(roots,name)
#         os.replace(source, target_path)
#         print(name)
#


# --------MP4, c_1_1 ,EthOutput---------


# path = r''
# for roots, dirs, files in os.walk(path):
#     for file in files:
#         source = os.path.join(roots,file)
#         name_file = os.path.basename(file)
#         name_file1 = name_file.split('_MP4')[0:]
#         name = ''.join(name_file1)
#         target_path = os.path.join(roots,name)
#         os.replace(source, target_path)
#         print(name)
#
#         source = os.path.join(roots, file)
#         name_file = os.path.basename(file)
#         name_file1 = name_file.split('_EthOutput')[0:]
#         name = ''.join(name_file1)
#         target_path = os.path.join(roots, name)
#         os.replace(source, target_path)
#
#
#
#         source = os.path.join(roots, file)
#         name_file = os.path.basename(file)
#         target_path1 =os.path.join(roots, name_file)
#         if '_c1_1.mf4' in name_file:
#             os.replace(source,target_path1)
#         else:
#             name_file1 = name_file.split('_c1_1')[0:]
#             name = ''.join(name_file1)
#             target_path = os.path.join(roots, name)
#             os.replace(source, target_path)


# source_dir = Path(r'Z:\Test')
# for file in source_dir.glob('*'):
#     if any([x in file.name for x in ['20211119', '20211125', '20211126', '20211129', '20211130']]):
#         file.replace(file.with_name(file.name.replace('X044', 'X043')))
#     if file.name.startswith('AP024') and '20211201' in file.name:
#         file.replace(file.with_name(file.name.replace('X044', 'X043')))
#
#     for files in file.glob('*'):
#         if any([x in files.name for x in ['20211119', '20211125', '20211126', '20211129', '20211130']]):
#             files.replace(files.with_name(files.name.replace('X044', 'X043')))
#         if files.name.startswith('AP024') and '20211201' in files.name:
#             files.replace(files.with_name(files.name.replace('X044', 'X043')))
#
#


# converted = ['B.mp4',  'B.webm.json' , '0000.webm' , '0000.webm.json' , '0001.webm', '0001.webm.json' , 'FrameNumber.csv' , '1.cap','GT.csv', 'OptiTrack.json' , 'SmartEye.json','0002.webm','0002.webm.json','LBL.csv','recalc.csv','0003.webm', '0003.webm.json','0004.webm', '0004.webm.json']
# raw = ['config.xml', '1.mf4', '1.json', 'placement.json']
# s = Path(r'')
# c = Path(r'')
#
# for dir in s.glob('*'):
#     print(dir)
#     destination = c / dir.name
#     print(destination)
#     for file in [x for x in list(dir.glob('*')) if any([x.name.endswith(s) for s in raw])]:
#         print(file)
#         shutil.move(file, destination)


# -----------------AP045_001_SQ5_TS007_20211217_MAX_static_X044_B_2021_12_17_130010#lc17130010q1a81ez------------
# source_dir = r'C:\Users\wjqbfc\Desktop\New_Folder'
# for roots, dirs, files in os.walk(source_dir):
#     for dir in dirs:
#         # source = os.path.join(roots, dir)
#         dir = dir.split('_')
#
#         if dir[8] =='B':
#              del dir[9:12]
#              name = '_'.join(dir)
#              name1 =name.split('#')
#
#              a = name1[0]
#              b = a.split('_')
#              del b[9]
#              new_name = '_'.join(b)
#              new_name = [new_name]
#              new_name.append(name1[1])
#              new_name1  = '#'.join(new_name)
#              print(new_name1)
# target_path = os.path.join(roots, new_name1)
#              os.replace(source, target_path)
# #
#
#
# p = r'C:\Users\wjqbfc\Desktop\New_Folder'
# for roots, dirs, files, in os. walk(p):
#     for dir in dirs:
#         source = os.path.join(roots, dir)
#         dir = dir.split('_')
#         if len(dir)  > 13:
#             del dir[7:]
#             file_new ='_'.join(dir)
#             print(file_new)
#             target_path = os.path.join(roots,file_new)
#             # os.replace(source,target_path)

