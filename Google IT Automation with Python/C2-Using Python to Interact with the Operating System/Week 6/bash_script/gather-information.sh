#!/bin/bash

# This code only for bash (LINUX)
line='------------------------------------------'
echo 'Starting at : $(date)'; echo $line

echo 'UPTIME'; uptime; echo $line

echo 'FREE'; free; echo $line

echo 'WHO'; who; echo $line

echo 'Finishing at: $(date)'