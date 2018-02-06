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


car_path = "/home/vivek/Documents/car_detection/cars_train/"
car_resize_path = "/home/vivek/Documents/car_detection/cars_train_resize/"

not_cars_path = "/home/vivek/Documents/car_detection/not_cars/"
not_cars_resize_path = "/home/vivek/Documents/car_detection/not_cars_resize/"

for root, dirs, files in os.walk(not_cars_path):
        for name in files:
            img = Image.open(os.path.join(root, name))
            img = img.resize((56, 56))
            img.save(not_cars_resize_path + name, quality=100)

for ind, file in enumerate(os.listdir(car_path)):
    if ind % 100 == 0:
        print(ind)
    img = Image.open(car_path + file)
    img = img.resize((56, 56))
    img.save(car_resize_path + file, quality=100)