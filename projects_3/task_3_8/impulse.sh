#!/bin/bash
read -p "Введите имя гена: " GENE_NAME
read -p "Введите уровень экспресси (целое число): " EXPRESSION_LEVEL 
echo "Экспрессия гена $GENE_NAME составляет $EXPRESSION_LEVEL единиц"
