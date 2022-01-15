#!/bin/sh
echo $1
echo $2

s=0

for i in $(seq $1); do s=$((s + i)); done

echo $s

