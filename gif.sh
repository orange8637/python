#!/bin/bash
# NAME:    gif (convert video to gif)
# USAGE:   ffmpeg -i input.ogv -vcodec libx264 output.mp4
#	       ./gif video.mp4

tmp=/tmp/$RANDOM
mkdir -p $tmp
ffmpeg -i "${1:?input is empty}" -r 4 $tmp/%06d.png
for i in $tmp/*.png
do
    convert $i $i.jpg
done
convert -delay 25 -loop 0 -fuzz 15% -layers Optimize $tmp/*.jpg "$1.gif"
rm -rf $tmp

