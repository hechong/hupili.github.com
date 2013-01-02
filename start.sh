#!/bin/bash
# Start the Jekyll for the current dir as background service. 

nohup jekyll --server &
PID=$!
echo $PID > jekyll-server.pid

exit 0 
