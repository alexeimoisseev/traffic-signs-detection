#!/bin/bash

mkdir -v -p data/SwedishSigns

if [ ! -f "data/SwedishSigns/Set1Part0.zip" ]; then
  curl -o data/SwedishSigns/annotations.txt 'https://www.cvl.isy.liu.se/research/trafficSigns/swedishSignsSummer/Set1/annotations.txt'
  curl -o data/SwedishSigns/Set1Part0.zip.part 'https://www.cvl.isy.liu.se/research/trafficSigns/swedishSignsSummer/Set1/Set1Part0.zip'
  mv -v data/SwedishSigns/Set1Part0.zip{.part,}
fi


mkdir -v -p data/SwedishSigns/images
mkdir -v -p data/SwedishSigns/labels
cd data/SwedishSigns/images
unzip ../Set1Part0.zip