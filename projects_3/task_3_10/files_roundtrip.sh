#!/bin/bash
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан файл: test${i}.txt"
done
count=10
    while [ $count -ge 1 ]; do
        rm "test${count}.txt"
        echo "Удален: test${count}.txt"
        count=$((count - 1))
done
