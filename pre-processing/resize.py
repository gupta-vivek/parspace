# -*- coding: utf-8 -*-
"""
@created on: 30/1/18,
@author: Vivek A Gupta,
@version: v0.0.1

Description:

Sphinx Documentation Status:

..todo::

"""

from PIL import Image
import os

# Parking Lot Image data path.
PKLot_path = "../../PKLot/PKLotSegmented"

# Parking Lot Image resized data path.
PKLot_resize_path = "../../PKLot_resize/"
PKLot_resize_empty_path = "../../PKLot_resize/Empty/"
PKLot_resize_occupied_path = "../../PKLot_resize/Occupied/"

# Number of files in PKLotSegmeted.
no_of_files = 695851
temp_a = round(no_of_files/10)
temp_b = round(temp_a/10)

count = 0
for root, dirs, files in os.walk(PKLot_path):
        print("Root - ", root.split('/')[-1])
        print("Dirs - ", dirs)
        print("Files - ", files)
        if root.split('/')[-1] == "Empty":
            PKLot_resize_path = PKLot_resize_empty_path
        elif root.split('/')[-1] == "Occupied":
            PKLot_resize_path = PKLot_resize_occupied_path
        for name in files:
            count += 1
            if round(count % temp_a) == 0:
                x = round(count/temp_b)
                print(str(x) + "% completed...")
            img = Image.open(os.path.join(root, name))
            img = img.resize((56, 56))
            img.save(PKLot_resize_path + name, quality=100)

# for ind, file in enumerate(os.listdir(car_path)):
#     if ind % 100 == 0:
#         print(ind)
#     img = Image.open(car_path + file)
#     img = img.resize((56, 56))
#     img.save(car_resize_path + file, quality=100)