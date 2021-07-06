# Softpage

I made this Project to provide Plagarism detection and similar stack features useful for Faculty and student usage.

Features:

* Online Plagarism Detection
* Offline Plagarism Detection
* Paraphrasing Text
* Summarising Text
* Execute/Modify Code

## Here is blog explaining working of [Softpage](https://r4hu1s0n7.hashnode.dev/softpage-and-how-its-made)

# Online Plagarism Detection Snapshot
uses file text3.txt from examples, and shows similarity.
![Shot1](https://github.com/r4hu1s0n7/Softpage/blob/main/examples/Screenshot%20(980).png)

# Offline Plagarism Detection Snapshot
uses file text1.txt as source and text2.txt main file from examples and shows similarity.
![Shot1](https://github.com/r4hu1s0n7/Softpage/blob/main/examples/Screenshot%20(985).png)

# Summarising Text
uses file text1.txt from examples and shows summary.
![Shot1](https://github.com/r4hu1s0n7/Softpage/blob/main/examples/Screenshot%20(984).png)

# Shows execution of Code
uses file F12.java from examples and shows output in prompt below.
![Shot1](https://github.com/r4hu1s0n7/Softpage/blob/main/examples/Screenshot%20(982).png)

# Pahaphrasing
uses model T5 condotional generator and retruns multiple versions of sentence
![Shot1](https://github.com/r4hu1s0n7/Softpage/blob/main/examples/Screenshot%20(1083).png)



# Dependencies
* tkinter
* spacy
* pandas
* nltk
* Beautiful soup
* en_web_core_sm nlp language model for spacy
* model phraser.pt and its dependencies used in paraphraser.py (if using paraphrasing)

Api used 
* [Google Search Rapidapi](https://rapidapi.com/apigeek/api/google-search3)
* [Text monkey summariser ](https://rapidapi.com/jhtong/api/text-monkey-summarizer)
