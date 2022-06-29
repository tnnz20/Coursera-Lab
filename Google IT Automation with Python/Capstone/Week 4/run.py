#!/usr/bin/env python3

import os
import requests

dir = 'supplier-data/descriptions'
url = "http://34.68.27.171/fruits/"

for filename in os.listdir(dir):
    if filename.endswith('.txt'):
        with open(os.path.join(dir,filename)) as opened:
            lines = opened.readlines()
            name = lines[0].strip()
            weight = int(lines[1].strip().replace(" lbs",""))
            description = lines[2].strip()
            image_name = filename.split(".")[0] + ".jpeg"
            data = {"name": name, "weight": weight, "description": description, "image_name": image_name}
            res = requests.post(url, data=data)
            print("status_code ",res.status_code)