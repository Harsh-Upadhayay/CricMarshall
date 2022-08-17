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
* Remove ffmpeg warning while recording voice
* Make list of extracted nouns (if neccesary)

16/08/2022:
* Extract year (if mentioned) from the generated text.

17/08/2022:
* Errors in extracted year. If the user only mention month and the year, the datefinder library automatically adding today's date. 
   i.e, if user says august 2016, then it will get extracted as 2016/08/17
* Voice of output generator is subject to change.

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

## Code Sources
* spech to text - https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
* noun extractor from text - https://www.codespeedy.com/proper-noun-extraction-in-python-using-nlp-in-python/
* text to speech convertor - https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3
