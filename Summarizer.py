try:
	import json
	import http.client
	import requests
except Exception as e:
	print("Import error")


# summarizer
def summarizer(load):

	payload = json.dumps({"text":load})
	conn = http.client.HTTPSConnection("text-monkey-summarizer.p.rapidapi.com")
	headers = {'content-type': "application/json",'x-rapidapi-key': "YOUR API KEY",'x-rapidapi-host': "text-monkey-summarizer.p.rapidapi.com"}
	conn.request("POST", "/nlp/summarize", payload, headers)
	res = conn.getresponse()
	data = res.read()
	data = json.loads(data)
	sdata="SUMMARY : \n\n"
	for i in data['summary'].split('\n'):
		if len(i)>15:
			sdata+='- '+i+'\n'

	return sdata
