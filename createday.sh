#!/bin/bash

dayNum=$(date +%-d)
yearNum=$(($(date +%-Y) - 2000))
yearFull=$(date +%-Y)

return_daily_path()
{
	mkdir -p ./AoC$3/day$4/$5/
	cp ./utils/$1.$2 ./AoC$3/day$4/$5/day$4.$2
}

echo "Creating setup for the day $dayNum"

if [ ! -d "AoC$yearNum/day$dayNum" ]
then
	mkdir "AoC$yearNum/day$dayNum"
else
	echo "Directory $dayNum already exists in directory AoC$yearNum"
	exit 0
fi

return_daily_path $"python_template" $"py" $yearNum $dayNum $"python"
cp -r ./utils/cpp_template ./AoC$yearNum/day$dayNum/cpp

sed -i "s/day_template/day$dayNum/" ./AoC$yearNum/day$dayNum/cpp/Makefile

curl -o ./AoC$yearNum/day$dayNum/input.txt -b session=$(cat .aocrc) -H "User-Agent: htiitinen94@gmail.com" https://adventofcode.com/$yearFull/day/$dayNum/input

cd ./AoC$yearNum/day$dayNum
cargo new rust

echo "Setup for year $yearNum day $dayNum is done!!!"
