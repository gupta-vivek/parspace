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

cars_resize_path = "/home/vivek/Documents/car_detection/cars_train_resize/"
not_cars_resize_path = "/home/vivek/Documents/car_detection/not_cars_resize/"

cars_array = []
not_cars_array = []

for index, file in enumerate(os.listdir(cars_resize_path)):
    if index % 500 ==0:
        print("Index - ", index)
    img = Image.open(cars_resize_path + file)
    cars_array.append([img, [1]])

fp = open("../data/cars", "w")
pickle.dump(cars_array, fp)
fp.close()
