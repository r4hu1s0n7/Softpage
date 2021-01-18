try:
	import http.client
	import json
	import requests
	import time
	import spacy
	import pandas as pd
	from bs4 import BeautifulSoup
	from nltk.corpus import stopwords
except:
	print("Import error")

def searchAPI(query):
	conn = http.client.HTTPSConnection("google-search3.p.rapidapi.com")
	links = []
	headers = {
	    'x-rapidapi-key': "921e1d2e2bmsh9e6ff57d02212fep1f88b6jsnfea9b1641599",
	    'x-rapidapi-host': "google-search3.p.rapidapi.com"
	    }

	query = query.replace(' ','%20').replace('\n','')

	conn.request("GET", "/api/v1/search/q="+query+"&num=7", headers=headers)

	res = conn.getresponse()
	data = res.read()

	data = data.decode("utf-8")
	data = json.loads(data)
	for i in data['results']:
		links.append(i['link'])
	return links




def saveScraped(links):
	with open(r'supports/out1.txt','w') as w:
		pass
	try:
		for i in links:
			if i[4:11] == 'youtube':
				continue
			with open(r'supports/out1.txt','a+',encoding='utf8') as o:#writes sample file for output comparision
				r = requests.get(i)
				time.sleep(5)
				sp = BeautifulSoup(r.content,features="lxml")
				geekdata = sp.find_all('p')
				geekdata = list(geekdata)
				o.write(str(geekdata[:]).lower().replace('<','').replace('>','').replace('/','').replace('&','').replace('=','').replace(':',''))
	except Exception as e:
		print(e)
	return	

def wordhash(word):
	return len(word)

def checkPlagarism(data1):

	with open(r'supports/out1.txt', 'r',encoding='utf8') as file:
		data2 = file.read()
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
				if word not in stop_words and word.pos_ in ('ADP','NOUN','PROPN','VERB') and len(word)>2:
					whlines.append(wordhash(word.lemma_))
					mklines += word.lemma_ + ' '
					
			# print(mklines)
			# print(whlines)
			
			if len(mklines)>0 and len(whlines)>3:
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
				if word not in stop_words and word.pos_ in ('ADP','NOUN','PROPN','VERB') and len(word)>2:
					whlines.append(wordhash(word.lemma_))
					mklines += word.lemma_ + ' '
					
			if len(mklines)>0 and len(whlines)>3:
				lines.append(mklines)
				hlines.append(whlines)
				d.append(2)
			mklines = ""
			whlines = []
	except Exception as e:
		print(e)
		return {'e':e,'m':"Error while processing"}


	try:
		frame = pd.DataFrame({"lines":lines,"hash":hlines,"doc":d})
		rows = len(frame.index)
		sums = []
		for i in range(rows):
		    rowsum = sum(frame.hash[i])
		    sums.append(rowsum)

		frame["hashes"] = sums
		frame = frame.sort_values(by='hashes')
		frame.to_csv(r'supports/frame.csv')
		frame = pd.read_csv(r'supports/frame.csv')
		same = 0
		k=[]
		for i in range(rows):
			
			for j in range(i+1,rows):

				if (frame.doc[i] != frame.doc[j]) and (frame.hashes[i] == frame.hashes[j]) and (frame.lines[i] == frame.lines[j]):
					k.append(frame.lines[i])
					same += 1
					break
				if (frame.hashes[i] != frame.hashes[j]):
					break
			
			if same == len1:
				break
	except Exception as e:
		print(e)
		return {'e':e,'m':"Error while calculating similarity"}
	with open('supports/log.txt', 'w') as f:
		for kk in k:
			f.write("%s\n" % kk)
	return (same/len1)
 
