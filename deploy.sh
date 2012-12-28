#!/bin/bash

# Remove temporary files from editors
find . -name "*~" -exec rm -f {} \;

git add . 
git commit -m "update blog`date`"
git push origin master

exit 0
