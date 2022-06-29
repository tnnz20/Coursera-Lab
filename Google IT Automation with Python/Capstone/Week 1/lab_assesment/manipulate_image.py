#!/usr/bin/env python3

# Import Library
from PIL import Image
import os

# Declare path
current_path_file = os.path.dirname(__file__)
file_dir = os.path.join(current_path_file, 'images/')
target_dir = os.path.join(current_path_file, 'new_images/')

# New Image format
format_img = '.jpeg'
res_img = (128,128)
rot_img = 90


def manipulate_image(file):
    for filename in os.listdir(file):
        if filename != '.DS_Store':
            im = Image.open(os.path.join(file_dir,filename))
            try:
                if os.path.isdir(target_dir) == False:
                    os.mkdir(target_dir)
            finally:
                im.resize(res_img).rotate(rot_img).convert('RGB').save(os.path.join(target_dir,filename+ format_img))

manipulate_image(file_dir)