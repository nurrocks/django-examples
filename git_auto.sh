#!/bin/bash



# loop
while true
do
# pers=$(stat -c %A README.md)
# if [ "$pers"  = "-rwxrwxrwx" ]; then  
#     eval "chmod 555 README.md"
# else
#     eval "chmod 777 README.md"
# fi

echo 1 >> README.md
eval "git commit -a -m 'change README'"
eval "git push"

# exec this script each 6000 seconds
sleep 12000
done