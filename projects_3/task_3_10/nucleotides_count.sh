#!/bin/bash
echo "-----------------------------------------------------------------"
printf "%-20s %7s %7s %7s %7s\n" "Файл" "A" "T" "G" "C"
echo "-----------------------------------------------------------------"
for file in *.fasta; do
    [ -e "$file" ] || continue
    if [ ! -s "$file" ]; then
        continue
    fi
    seq=$(grep -v "^>" "$file" | tr -d '\n\r\t ')
    count_A=$(echo "$seq" | grep -o "A" | wc -l)
    count_T=$(echo "$seq" | grep -o "T" | wc -l)
    count_G=$(echo "$seq" | grep -o "G" | wc -l)
    count_C=$(echo "$seq" | grep -o "C" | wc -l)
    printf "%-20s %7d %7d %7d %7d\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done
echo "-----------------------------------------------------------------"
