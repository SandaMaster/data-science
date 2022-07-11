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


def change_name_MAX(file_path):
     for roots, dirs, files in os.walk(file_path):

        for dir in dirs:
            if dir.startswith('AP0'):
                splited_dirs = dir.split('_')


                software = 'X044'
                hardware = 'B'




                if len(splited_dirs) == 7:
                    splited_dirs1 = splited_dirs[6].split('#')

                    test_subject = splited_dirs[0]
                    scenario_id = splited_dirs[3]
                    date = splited_dirs[4]
                    software_num = software
                    hardware_num = hardware
                    xylon_hash = splited_dirs1[1]



                elif len(splited_dirs) == 11:
                    splited_dirs1 = splited_dirs[10].split('#')

                    test_subject = splited_dirs[0]
                    scenario_id = splited_dirs[3]
                    date = splited_dirs[4]
                    software_num = software
                    hardware_num = hardware
                    xylon_hash = splited_dirs1[1]


                elif len(splited_dirs) == 13:
                    splited_dirs1 = splited_dirs[12].split('#')

                    test_subject = splited_dirs[0]
                    scenario_id = splited_dirs[3]
                    date = splited_dirs[4]
                    software_num = splited_dirs[7]
                    hardware_num = splited_dirs[8]
                    xylon_hash = splited_dirs1[1]


                elif len(splited_dirs) == 14:
                    splited_dirs1 = splited_dirs[13].split('#')

                    test_subject = splited_dirs[0]
                    scenario_id = splited_dirs[3]
                    date = splited_dirs[4]
                    software_num = splited_dirs[7]
                    hardware_num = splited_dirs[8]
                    xylon_hash = splited_dirs1[1]




                else:
                    print('Unhandled length of dirs')


                new_name = (f'{test_subject}_001_SQ5_{scenario_id}_{date}_MAX_static_{software_num}_{hardware_num}#{xylon_hash}')
                print(new_name)


            old_name_path = os.path.join(roots, dir)
            old_name = os.path.basename(dir)

            if os.path.isdir(old_name_path):
                new_path = old_name_path.replace(old_name, new_name )

                if dir != new_name:
                    os.rename(old_name_path, new_path)




        for file in files:
            splited_file = file.split('_')

            for element in splited_file:

                if len(element) == 6 and element.isdigit():
                    index = splited_file.index(element)
                    splited_file = splited_file[:index - 3] + splited_file[index + 1:]

            if 'sample' in splited_file:
                index = splited_file.index('sample')
                splited_file = splited_file[:index] + splited_file[index + 1:]

            if 'X044' not in splited_file:
                index = splited_file.index('static')
                splited_file.insert(index + 1, 'X044')
                splited_file.insert(index + 2, 'B')

            new_file = '_'.join(splited_file)
            print(new_file)

            splited_new_file = new_file.split('_')

            if 'B' in new_file:
                index = splited_new_file.index('B')
                splited_new_file = splited_new_file[index: ]

            splited_new_file = '_'.join(splited_new_file[1:])
            print(splited_new_file)

            source = os.path.join(roots,file)
            name_file = os.path.basename(file)
            if os.path.isfile(source):
                suf = os.path.basename(roots)
                suf = suf.split('#')[0]
                suffix = suf + splited_new_file
                destiny = source.replace(name_file, suffix)
                if file != destiny:
                    new_source = os.path.join(roots, destiny)
                    os.rename(source, new_source)



file_path = r''
change_name_MAX(file_path)

#
# ---------X043-----------------
#
# source_dir = Path(r'')
# for file in source_dir.glob('*'):
# if any([x in file.name for x in ['20211119', '20211122''20211125', '20211126', '20211129', '20211130']]):
#     file.replace(file.with_name(file.name.replace('X044', 'X043')))
# if file.name.startswith('AP024') and '20211201' in file.name:
#     file.replace(file.with_name(file.name.replace('X044', 'X043')))
#
# for files in file.glob('*'):
#     if any([x in files.name for x in ['20211119', '20211122', '20211125', '20211126', '20211129', '20211130']]):
#         files.replace(files.with_name(files.name.replace('X044', 'X043')))
#     if files.name.startswith('AP024') and '20211201' in files.name:
#         files.replace(files.with_name(files.name.replace('X044', 'X043')))
#
#
#
#
# ---------_B_-------------
#
#
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
#
#
# --------MP4, c_1_1 ,EthOutput---------
#
#
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
#
#
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
#
#
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
#
#
# ---------------------ŚMIECI------------------------#
#
#
# PLATFORM_SIGNAL_MAP = {"left_eye_occluded": {"not_labeled": 0, "eye_fully_visible": 1, "eye_fully_occluded": 2,
#                                              "occlusion0to25": 3, "occlusion25to50": 4, "occlusion50to100": 5},
#                        "right_eye_occluded": {"not_labeled": 0, "eye_fully_visible": 1, "eye_fully_occluded": 2,
#                                               "occlusion0to25": 3, "occlusion25to50": 4, "occlusion50to100": 5},
#                        "left_eye_detected": {"not_labeled": 0, "eye_not_detected": 1, "eye_detected": 2},
#                        "right_eye_detected": {"not_labeled": 0, "eye_not_detected": 1, "eye_detected": 2},
#                        "left_eye_detected_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                         "sure_based_on_driver_camera": 2,
#                                                         "sure_based_on_side_camera": 2},
#                        "right_eye_detected_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                          "sure_based_on_driver_camera": 2,
#                                                          "sure_based_on_side_camera": 2},
#                        "left_eye_closed": {"not_labeled": 0, "eye_not_closed": 1, "eye_closed": 2, "transition": 3},
#                        "right_eye_closed": {"not_labeled": 0, "eye_not_closed": 1, "eye_closed": 2, "transition": 3},
#                        "left_eye_closed_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                       "sure_based_on_driver_camera": 2, "sure_based_on_side_camera": 2},
#                        "right_eye_closed_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                        "sure_based_on_driver_camera": 2,
#                                                        "sure_based_on_side_camera": 2}, }
#
#
# signals_dict = {}
# actual_signal = {}
# with open('AP007_001_SQ5_TS015_20211122_MAX_static_c1_1_MP4_0000.xml', 'r', encoding='utf-8') as file:
#     xml = file.read()
#     dict = xmltodict.parse(xml)
#     x = dict['DM_Gen2']['OfflineLabelData']['OffLabel'][4]['Instance']['Property']
#
#     for signal_data in x:
#         signals_dict[signal_data['@Name']] = []
#
#         signal_name = signal_data['@Name']
#         signal_changes = signal_data['AtTime']
#         previus_frame_nuber = 0
#
#         for i in range(len(signal_changes)):
#             frame_number = signal_changes[i]['@FrameNumber']
#             try:
#                 next_frame_number = signal_changes[i + 1]['@FrameNumber']
#             except IndexError:
#                 pass
#
#             change_to_state = signal_changes[i]['ChangeTo']['@Value']
#             state_id = PLATFORM_SIGNAL_MAP[signal_name][change_to_state]
#
#             if frame_number.isdigit():
#                 frame_number = int(frame_number)
#             else:
#                 continue
#
#
#             if next_frame_number.isdigit():
#                 next_frame_number = int(next_frame_number)
#             else:
#                 next_frame_number = 0
#
#
#             if previus_frame_nuber < frame_number < next_frame_number:
#                 signals_dict[signal_data['@Name']].append((frame_number, state_id))
#                 previus_frame_nuber = frame_number
#             else:
#                 continue
#
#
#
# slownik = {}
# Lista1 = []
# Lista2 = []
# p = r'C:\Users\wjqbfc\Desktop\sad'
# for roots, dirs, files in os.walk(p):
#     for filr in files:
#         Lista1.append(filr)
# print(Lista1)
#
# for x in range(1, 6):
#     Lista2.append(x)
# print(Lista2)
#
# for i in Lista1:
#     slownik[i] = 0
# print(slownik)
#
# for z, z2 in zip(slownik.items(), Lista2):
#     key, value = z
#     if value == 0:
#         slownik[key] = z2
#
# print(slownik)
#
#
#
#
#
#
#
# PLATFORM_SIGNAL_MAP = {"left_eye_occluded": {"not_labeled": 0, "eye_fully_visible": 1, "eye_fully_occluded": 2,
#                                              "occlusion0to25": 3, "occlusion25to50": 4, "occlusion50to100": 5},
#                        "right_eye_occluded": {"not_labeled": 0, "eye_fully_visible": 1, "eye_fully_occluded": 2,
#                                               "occlusion0to25": 3, "occlusion25to50": 4, "occlusion50to100": 5},
#                        "left_eye_detected": {"not_labeled": 0, "eye_not_detected": 1, "eye_detected": 2},
#                        "right_eye_detected": {"not_labeled": 0, "eye_not_detected": 1, "eye_detected": 2},
#                        "left_eye_detected_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                         "sure_based_on_driver_camera": 2,
#                                                         "sure_based_on_side_camera": 2},
#                        "right_eye_detected_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                          "sure_based_on_driver_camera": 2,
#                                                          "sure_based_on_side_camera": 2},
#                        "left_eye_closed": {"not_labeled": 0, "eye_not_closed": 1, "eye_closed": 2, "transition": 3},
#                        "right_eye_closed": {"not_labeled": 0, "eye_not_closed": 1, "eye_closed": 2, "transition": 3},
#                        "left_eye_closed_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                       "sure_based_on_driver_camera": 2, "sure_based_on_side_camera": 2},
#                        "right_eye_closed_confidence": {"not_labeled": 0, "unsure": 1, "sure": 2,
#                                                        "sure_based_on_driver_camera": 2,
#                                                        "sure_based_on_side_camera": 2}, }
#
# signals_dict = {}
# actual_signal = {}
# frame_number_list = []
#
# with open('AP007_001_SQ5_TS015_20211122_MAX_static_c1_1_MP4_0000.xml', 'r', encoding='utf-8') as file:
#     xml = file.read()
#     dict = xmltodict.parse(xml)
#     x = dict['DM_Gen2']['OfflineLabelData']['OffLabel'][4]['Instance']['Property']
#
#     for signal_data in x:
#         signals_dict[signal_data['@Name']] = []
#
#         signal_name = signal_data['@Name']
#         signal_changes = signal_data['AtTime']
#
#         for i in range(len(signal_changes)):
#             first_frame_number = signal_changes[i]['@FrameNumber']
#             second_frame_number = signal_changes[i+1]['@FrameNumber']
#
#             first_frame_number = int(first_frame_number)
#             second_frame_number = int(second_frame_number)
#
#
#
# frame_number_list = iter(frame_number_list)
# first_frame_number = next(frame_number_list)
# second_frame_number = next(frame_number_list)
#
# first_frame_number1 = int(first_frame_number)
# second_frame_number2 = int(second_frame_number)
#
# if first_frame_number1 == 555885345:
#     del first_frame_number1
# else:
#     for missing_frame_number in range(first_frame_number1, second_frame_number2):
#         print(missing_frame_number)
#
# a = [1, 2, 3, 4]
# b = iter(a)
# c = next(b)
# d = next(b)
# e = next(b)
#
#
#
#
#
#
#
#
#
# note = r"C:\Users\wjqbfc\Desktop\list.txt"
# path = r"Z:\Synthetic movies"
#
# List2 =[]
# List = []
# lists = []
# source = []
# all_fill_STD =[]
#
# for roots, folders, files in os.walk(path):
#     for folder in folders:
#         if folder.endswith("beta"):
#             List.append(folder)
#
#     for folder1 in folders:
#         if folder1.endswith("1.1.3"):
#             List.append(folder1)
#
#
# with open(note, 'r', encoding="utf-8") as z:
#     dupa = z.read()
#     lists.append(dupa)
#
# for i in lists:
#     source.append(i.replace("\n", " "))
#
#
# splited = source[0].split(" ")
#
# for x in splited:
#     List2.append(x)
#
# print(len(List))
# print(len(List2))
#
# for z in List:
#     print(z)
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
#
#
#
#
#
#
#
#
# List_element =[]
#
# def find_all(path):
#     for roots, folders, files in os.walk(path):
#         for file in files:
#             source = os.path.join(roots, file)
#             with open(source, 'r', encoding="utf-8") as x:
#                 for line in x:
#
#                     ingest_index = line.find("ingest")
#                     film_index = line.find('a310')
#                     film_index2 = line.find('a350')
#                     film_index3 = line.find('a3c8')
#
#                     if ingest_index > 0:
#                         id = line[ingest_index + 7:ingest_index + 13]
#                         if id.isdigit():
#                             print(id)
#                             List_element.append(id)
#
#
#                     if film_index > 0:
#                         film = line[film_index + 5 :film_index + 100 ]
#                         if film.startswith('AP'):
#                             print(film)
#                             List_element.append(film)
#
#                     if film_index2 > 0:
#                         film2 = line[film_index2 + 5 :film_index2 + 100 ]
#                         if film2.startswith('AP'):
#                             print(film2)
#                             List_element.append(film2)
#
#
#                     if film_index3 > 0:
#                         film3 = line[film_index3 + 5 :film_index3 + 100 ]
#                         if film3.startswith('AP'):
#                             print(film3)
#                             List_element.append(film3)
#
#
# path = r"C:\Users\wjqbfc\Desktop\gmdm"
# find_all(path)
# p = r"Z:\Synthetic movies"
#
#
#
#
#
# for roots, folders, files in os.walk(p):
#     for folder in folders:
#         if folder.startswith("SN"):
#             splited_folder = folder.split("SX")
#             source = os.path.join(roots, folder)
#             joined_folder = "S7".join(splited_folder)
#             destiny = os.path.join(roots, joined_folder)
#
#             os.rename(source, desti
#
#
#
#
#
#
#
# path_to_converted = r'Y:\Data_collection_raw'
# path_to_actual = r'Y:\Data_collection'
# output_dir_dirs = set(os.listdir(path_to_converted))
# dirs_in_actual= set(os.listdir(path_to_actual))
#
# dirs_to_create = dirs_in_actual - output_dir_dirs
#
# for dir in dirs_to_create:
#     os.mkdir(f"{path_to_converted}/{dir}")
#
#
#
#
#
#
# def mdf_to_mp4(path):
#     for roots, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith('c1_1.mf4'):
#                 file_path = os.path.join(roots, file)
#                 a = file_path.split('\\')
#                 dir_path = '\\'.join(a[:-1])
#                 file_path = file_path.replace('\\', '/')
#                 cmd = f"dotnet C:/Users/wjqbfc/repos/toolchain_scripts/max_mdf_to_mp4_converter/bin/Release/netcoreapp2.2/MDF4ToMp4Converter.dll -i {file_path} -o {dir_path} -c"
#                 print(cmd)
#                 os.system(cmd)
#
#
# path = r'C:\Users\wjqbfc\Desktop\New_Folder'
# mdf_to_mp4(path)
#






path = r"C:\Users\wjqbfc\Desktop\Push mdm\csvki.txt"
with open(path, 'r') as csvfile:
    measure = [l for l in csvfile.readlines()]
    measure_list = list(set(measure))
    for i in measure_list:
        print(i)








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

    def obwod(self):
        return 2*self.b+2*self.a

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
