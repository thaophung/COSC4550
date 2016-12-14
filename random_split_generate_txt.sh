#!/bin/bash


# Requirements
# 1. Install gshuf for Mac: brew install coreutils
# more info: http://apple.stackexchange.com/questions/142860/install-shuf-on-os-x


mkdir -p train
mkdir -p val


for d in `ls -d training_set/*`; do 

  echo ${d}

  # Directory name is also label
  label=$(basename $d)
  
  # Number of items in label
  num=`ls -l ${d} | wc -l`
  #echo $num
  train_num=$((90 * $num / 100))
  val_num=$((10 * $num / 100))
  echo "Label: ${label}"

  # 0. Make directories for train/val
  mkdir -p val/${label}
  mkdir -p train/${label}

  # 1. Move N=val_num random images to validation
  val_dir=val/${label}
  for f in `ls ${d}/*.JPEG | gshuf | head -$val_num`; do 
    echo "val_num"
    mv ${f} ${val_dir}
    echo "Done"
  done    # Note the command is "mv", ie. it will move files permanently
  #mv `ls ${d}/*.JPEG | gshuf | head $val_num` ${val_dir}
  echo "val: `ls ${val_dir}/*.JPEG | wc -l` files"

  # 2. Move N=train_num random images to validation
  train_dir=train/${label}
  for f in `ls ${d}/*.JPEG | gshuf | head -$train_num`; do 
    #echo "train_dir"
    mv ${f} ${train_dir}
  done
  #mv `ls ${d}/*.JPEG | gshuf | head $train_num` ${train_dir}
  echo "train: `ls ${train_dir}/*.JPEG | wc -l` files"

  # 3. Generate txt files for val
  for f in `ls val/${label}/*.JPEG | gshuf`; do 
    echo "${f} ${label}" >> txt_val_${label}.txt
  done

  # 4. Generate txt files for train
  for f in `ls train/${label}/*.JPEG | gshuf`; do 
    echo "${f} ${label}" >> txt_train_${label}.txt
  done

  # 5. Here manually examine if the txt files look good (links are valid, and labels are correct)
  # 6. Finally concat all txt_val_*.txt into one val.txt using a bash command
  cat txt_val_*.txt > val.txt
  gshuf val.txt > val.txt.shuf 
  mv val.txt.shuf val.txt
  # 7. Finally concat all txt_train_*.txt into one train.txt using a bash command
  cat txt_train_*.txt > train.txt
  # The end. 

done
