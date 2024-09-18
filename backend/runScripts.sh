#!/bin/bash

# Run main.py
rm study_guide.md
rm output.mp3
cd questionShuffler
python3 main.py

# Run studyGuideGenerator.py
cd ..
echo "Would you like to run studyGuideGenerator? (Y/N)"
read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    python3 studyGuideGenerator.py
else
    echo "Skipping studyGuideGenerator."
fi
cd questionShuffler
rm failed_questions.txt
cd ..

echo "Would you like to run readToMe? (Y/N)"
read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    python3 readToMe.py
else
    echo "Skipping readToMe."
fi

#play output.mp3
mpg123 output.mp3


