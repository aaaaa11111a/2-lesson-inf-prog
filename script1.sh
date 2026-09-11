#!/bin/bash
read N
for i in $(seq 1 $N)
do 
a=$RANDOM
b=$RANDOM
echo "$a + $b = $(($a + $b))" > file$i.txt
done
