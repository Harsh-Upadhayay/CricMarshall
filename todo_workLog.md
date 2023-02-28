## To-Do List
15/08/2022: 

- [ ] Remove ffmpeg warning while recording voice
- [x] Make list of extracted nouns (if neccesary)

16/08/2022:
- [x] Extract year (if mentioned) from the generated text.

17/08/2022:
- [ ] Errors in extracted year. If the user only mention month and the year, the datefinder library automatically adding today's date. 
   i.e, if user says august 2016, then it will get extracted as 2016/08/17
- [x] Voice of output generator is subject to change.

19/08/2022
- [ ] create small database to run queries and analyze the result
- [x] got suggestion to work on pandas for query processing and result generation. Discussion required.
    - Pandas used as primar data processor.

05/09/2022
- [x] Using Parsing: Get POS tags of every word of the input. Define a structure of the sentence (for ex. sentence = Noun + Adjective + Verb + ... ). Generate a sentence using the input. The generated sentence will be used to fetch the required result.
- [x] Query Processing: pandas or mongodb (Decision Pending)
    - Pandas

14/09/2022
- [x] parse input query to fetch result.

- [x] Add Strike Rate in Batsman
- [x] Add No Balls, Wides and Economy in Bowler
    *Extra runs are COUNTED as "Runs conceded by Bowler". 
    *Extra run is NOT COUNTED as "run scored by batsman".
    *Extra ball is NOT COUNTED as "ball bowled by bowler". 
    
- [x] (In case of NO BALL)
        *Extra runs = extra runs + 1
        *balls played by batsman: balls = balls + 1
        *if runs are scored on the NO BALL: runs scored by batsman: runs = runs + (amount of runs scored)
        *runs conceded by bowler = runs = runs + (amount of runs conceded)

05/11/2022
- [ ] Use viterbi to find player's current team.
- [ ] Support  parsing of multiple type of querys.
    
"""

## Work Log
15/08/2022: 
* Speech to text regonition, first with audio file and then with using microphone.
* Removed stopwords and tagged the remaining meaningfull words as noun,verb etc.
* Extracted nouns for query processing.
* Extended the voice input duration from 5 sec to 10 sec.

16/08/2022:
* Added date extractor but it has errors to remove.
* Year is getting extracted through 'CD' tag. Need discussion over this.

17/08/2022:
* Output Generator added. Converting text to speech in US English.
* setup file added (2 lines of code to download nltk libraries on remote device).
* Voice speed reduced. 200 was default. now its 195.

05/09/2022:
*  "Wake UP Marshall x Marshall Never Sleep" Added. Intro message Added.
*  Seperation of concerns is done in input.py and added InputParsing.py for the same

14/09/2022
* added code to run the voice input until user say thank you.

09/11/2022
* Project stage - 1 DONE for NLP semester-5
* Project Report - 1 submission

## Dataset sources 

  *  https://www.kaggle.com/datasets/narendrageek/can-generate-automatic-commentary-for-ipl-cricket?select=IPL_Match_Highlights_Commentary.csv
