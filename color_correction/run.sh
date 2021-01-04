#!/usr/bin/env sh
python3 extract_images.py
mkdir in2
for  x in  in/*.jpg ;do echo "$x"; cp "$x" "in2/${x:58}" ;done
python3 conv_binary.py

