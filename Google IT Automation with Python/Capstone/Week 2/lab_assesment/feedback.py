#!/usr/bin/env python3

# import library
import os
import requests

# curent file
current_path_file = os.path.dirname(__file__)


feedback_coloumn = ['title', 'name', 'date', 'feedback']
feedback_dir = os.path.join(current_path_file, 'feedback/')

for file in os.listdir(feedback_dir):
    with open(os.path.join(feedback_dir, file)) as f:
        txt_list = []
        lines = f.readlines()
        for line in lines:
            txt_list.append(line.strip())
        
        # zip keys and txt into dictionary
        feedback = dict(zip(feedback_coloumn, txt_list))

        # post feedback with requests
        res = requests.post('http://35.224.50.184/feedback/', data=feedback)
        print("status_code ",res.status_code) 