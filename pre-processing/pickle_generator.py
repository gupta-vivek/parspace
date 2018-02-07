# -*- coding: utf-8 -*-
"""
@created on: 31/1/18,
@author: Vivek A Gupta,
@version: v0.0.1

Description:

Sphinx Documentation Status:

..todo::

"""

import os
import pickle
from PIL import Image

empty_path = "../../PKLot_resize/Empty/"
occupied_path = "../../PKLot_resize/Occupied/"

empty_files = 358071
occupied_files = 337780


def pickle_gen(data_path, label, no_of_files, save_path):
    count = 0
    temp_a = round(no_of_files / 10)
    temp_b = round(temp_a / 10)
    temp_array = []
    for index, file in enumerate(os.listdir(data_path)):
        count += 1
        if round(count % temp_a) == 0:
            x = round(count / temp_b)
            print(str(x) + "% completed...")
        img = Image.open(data_path + file)
        temp_array.append([img, [label]])

        fp = open(save_path, "w")
        pickle_generator.dump(temp_array, fp)
        fp.close()

pickle_gen(empty_path, 0, empty_files, "../data/empty")
pickle_gen(occupied_path, 1, occupied_files, "../data/occupied")