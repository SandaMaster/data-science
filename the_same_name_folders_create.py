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



path_to_converted = r'Y:\Data_collection_raw'
path_to_actual = r'Y:\Data_collection'
output_dir_dirs = set(os.listdir(path_to_converted))
dirs_in_actual= set(os.listdir(path_to_actual))

dirs_to_create = dirs_in_actual - output_dir_dirs

for dir in dirs_to_create:
    os.mkdir(f"{path_to_converted}/{dir}")

