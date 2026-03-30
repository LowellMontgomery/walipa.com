# A simple script to pad your current filenames to 8 digits
# Run this inside your /seeds directory
for f in [0-9][0-9][0-9]_*.md; do
    num=$(echo $f | cut -d'_' -f1)
    rest=$(echo $f | cut -d'_' -f2-)
    new_num=$(printf "%08d" $num)
    mv "$f" "${new_num}_${rest}"
done