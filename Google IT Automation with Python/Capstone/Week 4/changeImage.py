#!/usr/bin/env python3

# Import Library
from PIL import Image
import os

file_dir = 'supplier-data/images'

format_img = '.jpeg'
res_img = (600,400)

for filename in os.listdir(file_dir):
    if filename.endswith('.tiff'):
        im = Image.open(os.path.join(file_dir, filename))
        im = im.convert('RGB')
        im = im.resize(res_img)
        im.save(os.path.join(file_dir, filename.split('.')[0] + format_img))