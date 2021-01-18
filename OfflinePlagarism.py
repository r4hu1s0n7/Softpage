try:
	import json
	import spacy
	import pandas as pd
	import os
	from tkinter import filedialog
	from nltk.corpus import stopwords
except:
	print("Import error")

# Provides hash value
def wordhash(word):
	return len(word)


# Performs the plagarism check
def checkPlagarism(data1,data2):
	try:
		stop_words = set(stopwords.words('english'))
		nlp = spacy.load("en_core_web_sm")
		doc = nlp(data1)
		lines = []
		hlines = []
		sents = list(doc.sents)
		len1 = len(sents)

		doc2 = nlp(data2)
		sents2 = list(doc2.sents)
		len2 = len(sents2)
	except Exception as e:
		print(e)
		return {'e':e,'m':"Language model error"}

	d = []
	sents =  sents + sents2

	try:
		mklines=""
		whlines=[]

		for line in sents:
			# print(line)
			for word in line:
				if word not in stop_words and word.pos_ in ('ADP','NOUN','PROPN','VERB'):
					whlines.append(wordhash(word.lemma_))
					mklines += word.lemma_ + ' '
			
			if len(mklines)>0:
				lines.append(mklines)
				hlines.append(whlines)
				d.append(1)
			mklines = ""
			whlines = []


		mklines=""
		whlines=[]
		for line in sents2:
			# print(line)
			for word in line:
				if word not in stop_words and word.pos_ in ('ADP','NOUN','PROPN','VERB'):
					whlines.append(wordhash(word.lemma_))
					mklines += word.lemma_ + ' '
					
			if len(mklines)>0:
				lines.append(mklines)
				hlines.append(whlines)
				d.append(2)
			mklines = ""
			whlines = []
	except Exception as e:
		print(e)
		return {'e':e,'m':"Error while processing"}
	try:
		sameones = []
		frame = pd.DataFrame({"lines":lines,"hash":hlines,"doc":d})
		rows = len(frame.index)
		sums = []
		for i in range(rows):
		    rowsum = sum(frame.hash[i])
		    sums.append(rowsum)

		frame["hashes"] = sums
		frame = frame.sort_values(by='hashes')
		frame.to_csv('supports/frame.csv')
		frame = pd.read_csv('supports/frame.csv')
		same = 0
		for i in range(rows):

			for j in range(i+1,rows):
				if  (frame.doc[i] != frame.doc[j]) and (frame.hashes[i] == frame.hashes[j]) and (frame.lines[i] == frame.lines[j]):
					sameones.append(frame.lines[j])
					
					break
				if (frame.hashes[i] != frame.hashes[j]):
					break
			if same == len1 or same == len2:
				break			

		sameones = set(sameones)
		same = len(sameones)
		similarity = same/min(len1,len2)
	except Exception as e:
		print(e)
		return {'e':e,'m':"Error while checking similarity"}

	with open('supports/log.txt', 'w') as f:
		for kk in sameones:
			f.write("%s\n" % kk)
	return {'p':similarity,'s':sameones} 


# Second source file provider
def secondFile():
	try:
		label=""	
		data=""
		file = filedialog.askopenfilename(filetypes=[('All Files','*.*')])
		label= os.path.basename(str(file))
		with open(file,encoding='utf8') as f1:
			data = f1.read()
	except Exception as e:
		print(e)
		data = "Error while opening file"
		return [6,data,label]
	return [100,data,label]
