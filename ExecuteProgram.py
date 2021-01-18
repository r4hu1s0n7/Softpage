try:
	import os
	import subprocess as sub
	from tkinter import filedialog
except:
	print("Import error")
pi=None
def startExecution(file,query):
	try:
		fname = ""
		fname = str(file)
		ix = fname[fname.rindex('.'):]
		path=os.path.dirname(file)
		path=os.path.normpath(path)
		fname = os.path.basename(str(file))
		print(path,fname)
		execs = ""
	except Exception as e:
		print(e)
		return [3,'Error while getting file']

	try:
		print()
		if ix == '.py':
			execs = 'python '+path+'\\'+fname + ' ' + query
			pi= sub.Popen(execs)
			
		elif ix == '.java':
			execs = 'javac '+path+'\\'+fname
			pi = sub.Popen(execs)
			print(execs)
			execs = "java "+fname[:fname.rindex('.') ] + ' ' + query
			print(execs)
			pi = sub.Popen(execs,cwd=path)

		elif ix == '.c':
			execs = 'gcc -o FileZZ ' +fname + ' ' + query
			pi = sub.Popen(execs,cwd=path)
			pi = sub.Popen('FileZZ',cwd=path)

		elif ix == '.html':
			execs = path + '\\'+fname
			pi = os.system(execs)
			return

		elif ix == '.cpp':
			execs = 'g++ -o FileZZ ' +fname + ' ' + query
			pi = sub.Popen(execs,cwd=path)
			pi = sub.Popen('FileZZ',cwd=path)

		else:
			return [5,'Execute this type of File using Another software']
			

	except Exception as e:
		print(e)
		return [4,'Error while Running']
	
	return [100,pi]
	


def readCode(file):
	fname = str(file)
	ix = fname[fname.rindex('.'):]
	data=""
	if ix in ('.py','.java','.c','.cpp','.html'):
		with open(file,encoding='utf8') as f1:
			data=f1.read()
	else:
		return [1,'This File cannot be opened']
	return [100,data]


def selectFile():
	try:
		runfile = filedialog.askopenfilename(filetypes=[('All Files','*.*')])
	except Exception as e:
		print(e)
		return [2,'Error while opening File']
	return [100,runfile]
