#!/usr/local/bin/bash
# convert.sh
# Apply tempo filter to .mp3 files in this and all sub directories
# Optional: Delete original file after conversion

shopt -s globstar
i=1
for song in ./**/*.mp3
do
  ffmpeg -loop 1 -i "default.jpg" -i "$song" -shortest -vf scale="trunc(oh*a/2)*2:720" -c:v libx264 -c:a copy "$song".mp4
  i=$((i+1))
done
