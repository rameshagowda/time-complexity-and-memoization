#! /bin/bash

N=10
f0=0
f1=1

echo "The Fibonacci series is.. "
for ((i=0; i<$N; i++))
do
	echo $f0
	fn=$((f0+f1))
	f0=$f1
	
done
