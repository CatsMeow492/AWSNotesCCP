#!/bin/bash

# Run main.py
rm study_guide.md
rm output.mp3
cd questionShuffler
python3 main.py

# Run studyGuideGenerator.py
cd ..
python3 studyGuideGenerator.py
cd questionShuffler
rm failed_questions.txt
cd ..

python3 readToMe.py

#play output.mp3
mpg123 output.mp3


