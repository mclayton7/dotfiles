#!/bin/bash
for file in *.jpg; do
    convert -enhance -equalize -contrast $file "${file%.jpg}_new.jpg"
done
