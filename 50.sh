/usr/bin/python3 "/Users/ruhidoshi/Desktop/study material /sf codes/49.py"
#!/bin/bash
echo Enter Directory name
read d
mkdir $d
echo enter number of files
read n
for((i=0;i<n;i++))
do
echo Enter file name
read f
cp $f $d
done
