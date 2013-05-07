#!/bin/bash
#
# ref: 
#    * http://stackoverflow.com/questions/6537490/insert-a-line-at-specific-line-number-with-sed-or-awk
#

for file in `find ../_posts -name "*.md"`
do 
	echo $file
ed $file << END
2i
group: blog
.
w
q
END
done

