#!/bin/bash

for file in *.txt; do
  sed -i.bak 's/.*/[&]/' $file
  sed -i.bak 's/.\(.\)$/\1/' $file
done

rm *.bak

rename "s/.txt/.json/" *.txt
