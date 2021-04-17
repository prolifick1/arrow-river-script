# Rename all *.mp3.mp4 to *.mp4
for f in *.mp3.mp4; do 
    mv -- "$f" "${f%.mp3.mp4}.mp4"
done
