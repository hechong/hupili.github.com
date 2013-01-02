#!/bin/bash
# Stop the Jekyll server running in the current dir

PID=`cat jekyll-server.pid`
echo "killing $PID"
kill $PID

exit 0
