# CricMarshall
Your cricket buddy!


## Developers Notes

* If match tied then two outcomes are possible, elimination("Eliminator") by superover or tie, handle both queries.
* Basic necessities of query : 
    * 2 Team names
    * Year of match
* Use UAG/ UCG to store first and second names of cricketers.

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

## Query Types
### Specific or Exact Queries :
    * Attributes : PlayerName, Year, PlayersTeam, OppositeTeam, Venue, Runs, Wickets, GameType, SeriesType
    * Example1 : How many runs did Rohit Sharma scored against Australia in 2016 on Sydney Cricket Ground ?
    * Example2 : How many wickets Jasprit Bumrah took on England tour of India in the year 2020 ? (Gametype Missing: T20, Test, ODI)

### LittleAmbiguousQueries : 
    * Attributes : PlayerName, Year, PLayersTeam, OppositeTeam, Venue, Runs, Wickets, GameType, SeriesType, DeciderWord(Highest, Lowest, Most etc)
    * Example1 : Who was the highest wicket taker in 2011 Cricket World Cup ?
        (Attributes available : Year = 2011, SeriesType = Cricket World Cup, DeciderWord = highest)
        (Derivable Attributes : GameType = ODI (Because in 2011, only one cricket world cup was oraganized and it was ODI world cup))
        (
            PossibleApproach : ((((***DISCUSTION REQUIRED***))))
                Pre-Requisite : we have scorecard of every match of the worldcup 2011. 
                1. select bowlerName, Wickets from EveryMatch
                1.1 If the same bowler has played multiple matches : Update the wicket column for this entry.
                2. select bowlerName from NewlyCreatedTable where wickets = (select max(Wickets) from NewlyCreatedTable)            
        )

## Required Libraries
* os 
* speech_recognition
* nltk
* datefinder
* string
* yaml
* pydub
* pyttsx3
* datetime
* pickle
* math
* ast(Abstract Syntax Tree)
* pandas
* 

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

## Code Sources
* spech to text - https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
* noun extractor from text - https://www.codespeedy.com/proper-noun-extraction-in-python-using-nlp-in-python/
* text to speech convertor - https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3
