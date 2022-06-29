#!/usr/bin/env python3

import requests
import os

dir = 'supplier-data/images'
url = "http://localhost/upload/"

for filename in os.listdir(dir):
    if filename.endswith('.jpeg'):
        with open(os.path.join(dir, filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(f'STATUS CODE {r.status_code}')