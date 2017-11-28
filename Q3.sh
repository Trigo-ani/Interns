#!/bin/sh

df -h > ani.txt

awk '{print $1 "," $2 "," $3 "," $4 "," $5 "," $6}' ani.txt > output.csv
