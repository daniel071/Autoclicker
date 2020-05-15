#!/bin/bash

mkdir bin.build
python3 -m nuitka --standalone --remove-output --output-dir=bin.build main.py
if [[ "$OSTYPE" == "darwin"* ]]; then
	mv ./autoClicker.bin ./bin.build/autoClicker_osx
	sudo codesign -f -s - ./bin.build/autoClicker.dist/Python
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	mv ./autoClicker.bin ./bin.build/autoClicker_linux
else
	mv ./autoClicker.bin ./bin.build/autoClicker
fi

cp -r ./Music ./bin.build/DungeonCli.dist/
cp -r ./Sounds ./bin.build/DungeonCli.dist/
