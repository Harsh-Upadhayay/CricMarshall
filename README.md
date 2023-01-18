# CricMarshall
Your cricket buddy! 

## Developers Notes

* If match tied then two outcomes are possible, elimination("Eliminator") by superover or tie, handle both queries.
* Basic necessities of query : 
    * 2 Team names
    * Year of match
* Use UAG/ UCG to store first and second names of cricketers.

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


## Code Sources
* spech to text - https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
* noun extractor from text - https://www.codespeedy.com/proper-noun-extraction-in-python-using-nlp-in-python/
* text to speech convertor - https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3
