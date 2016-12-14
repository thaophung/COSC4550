#!/bin/bash

for d in `ls -d test/*`; do
  echo ${d}

  #Directory name is also label
  label=$(basename $d)

  for f in `ls train_10_image/${label}/*.JPEG | gshuf`; do
    echo "${f} ${label}" >> test.txt
  done
done
