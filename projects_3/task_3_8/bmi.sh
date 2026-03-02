#!/bin/bash
read -p "Введите массу тела (в кг): " mass
read -p "Введите рост (в метрах): " height
bmi=$(echo "$mass/($height * $height)" | bc)
echo "Ваш индекс массы тела: $bmi"
