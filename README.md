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
![Screenshot (980)](https://github.com/r4hu1s0n7/Softpage/assets/40057302/eb47e9ca-09d8-4800-9ff3-ef71b06eaac4)

# Offline Plagarism Detection Snapshot
uses file text1.txt as source and text2.txt main file from examples and shows similarity.
![Screenshot (985)](https://github.com/r4hu1s0n7/Softpage/assets/40057302/0905c63d-9ae9-4991-85b5-478fec487a3a)


# Summarising Text
uses file text1.txt from examples and shows summary.
![Screenshot (984)](https://github.com/r4hu1s0n7/Softpage/assets/40057302/cba1426c-c00c-4403-9f1f-e6525dc850dc)

# Shows execution of Code
uses file F12.java from examples and shows output in prompt below.
![Screenshot (982)](https://github.com/r4hu1s0n7/Softpage/assets/40057302/8d7c062a-ba52-4ddd-9afb-1c5b9d7c028b)


# Pahaphrasing
uses model T5 condotional generator and retruns multiple versions of sentence
![Screenshot (1083)](https://github.com/r4hu1s0n7/Softpage/assets/40057302/a4d5df67-faef-4480-a265-f35c2d8f0089)




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
