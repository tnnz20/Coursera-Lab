#!/usr/bin/env python3

import re
import csv
import operator
import os

# Error Message
error = {}

# Count message by user
per_user = {}

# Local Path file
path = os.path.dirname(__file__)

# Open log file
with open(os.path.join(path, 'syslog.log')) as file :
    logs = file.readlines()
    for log in logs:
        # Create regex pattern to find INFO or ERROR log
        match = re.search(r"ticky: (INFO|ERROR) (.*) \((.*)\)", log.strip())

        if match != None:
            log_type = match.group(1)
            message = match.group(2).strip()
            username = match.group(3).strip()
            (value_info,value_error) = per_user.get(username,(0,0))
            
            if log_type == 'ERROR':
                # add message to variable error
                if message not in error:
                    error[message] = 0
                error[message] += 1
                value_error +=1
            else:
                value_info +=1
            
            per_user[username] = (value_info,value_error)
                
file.close()

errors = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
per_user = [(key,val[0],val[1])for key, val in sorted(per_user.items(), key = operator.itemgetter(0))] 

with open(os.path.join(path,"error_message.csv"), 'w+') as errors_file:   
    writer = csv.writer(errors_file)
    writer.writerow(("Error", "Count"))
    writer.writerows(errors)
errors_file.close()

with open(os.path.join(path,"user_statistics.csv"), 'w+') as users_file:   
    writer = csv.writer(users_file)
    writer.writerow(("Username", "INFO", "ERROR"))
    writer.writerows(per_user)
users_file.close()     