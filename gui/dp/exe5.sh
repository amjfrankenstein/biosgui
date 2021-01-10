#!/bin/bash
unbuffer dpcmd --type W25Q64BV -u ~/BiosUnlocking/Dell/e6440/8.bin -v |& tee -a output.txt
if grep -q Error output.txt; then
    espeak -p 9 -s 190 'chip write failed'
else
    espeak -p 9 -s 190 'chip write successful'
fi
rm output.txt
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ;
else 
echo 'goodbye' ;
exit
fi 
done

