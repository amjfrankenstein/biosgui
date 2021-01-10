#!/bin/bash
unbuffer dpcmd --type EN25QH32 -e |& tee -a output.txt
if grep -q Error output.txt; then
    espeak -p 9 -s 190 'erasure failed'
else
    espeak -p 9 -s 190 'erasure completed'
fi
rm output.txt
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ; 
else 
echo 'goodbye'
exit 
fi 
done
