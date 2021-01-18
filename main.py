# SoftPage | Build 2.0 | by Rahul Soni | 13 - January - 2021 
try:
	import os
	import json
	import tkinter as T
	from tkinter.ttk import *
	from tkinter import filedialog,messagebox
	import OnlinePlagarism as On
	import OfflinePlagarism as Of
	import Summarizer as Sm
	import ExecuteProgram as Ep
except Exception as e:
	print(e)

class Mains():


# this will display input content into text area
	def show(self,data):
		try:
			self.lshow.delete('1.0',T.END)
			self.lshow.insert(T.END,data)
		except:
			messagebox.showinfo('Attention','Error while loading Assignment')
		return

	def fun(self,ch):
		return ch in ['T']


# fill up files of selected directory
	def fillSelectionBox(self):
		global xz
		try:
			self.lst.delete(0,'end')
			xz = filedialog.askdirectory()
			flist=os.listdir(xz)
			for item in flist:
				self.lst.insert(T.END,item)
		except Exception as e:
			print(e)
			messagebox.showinfo('Attention','Error while opening Directory')
			return 
		return


# open selected file in text area
	def openSelected(self):
		global xz
		read=""
		self.lshow.delete('1.0',T.END)
		try:
			with open(xz+'/'+str(self.lst.get(self.lst.curselection()[0])),'rb') as f1:
					lne = f1.read()
					data = lne.decode('utf8')
					self.show(data)
					self.reads = data
		except Exception as e:
			print(e)
			messagebox.showinfo('Attention','Error while Opening Assignment')
		return


# clears everything
	def clearpad(self):
		self.lshow.delete('1.0',T.END)
		self.selfile['text'] = ""
		self.srcfile = ""
		self.reads = ""
		self.gclr()
		self.process.kill()
		self.process = None
		return


# selectes 2nd file for offline plagarism
	def secondFile(self):
		data = Of.secondFile()
		if data[0] == 100:	
			self.srcfile = data[1]
			self.selfile['text']= data[2]
		else:
			messagebox.showinfo("Attention",data[1])
		return


# enables and disables buttons
	def runtoggle(self,x):
		if x == 1:
			self.runsv['state'] = 'normal'
			self.runcmd['state'] = 'normal'
			self.runstop['state'] = 'normal'
		else:
			self.runcmd['state'] = 'disabled'
			self.runsv['state'] = 'disabled'
			self.runstop['state'] = 'disabled'			
		return
	def basictoggle(self,x):
		if x == 1:
			self.brw['state'] = 'normal'
			self.sel['state'] = 'normal'
			self.gqry['state'] = 'normal'
		else:
			self.brw['state'] = 'disabled'
			self.sel['state'] = 'disabled'
			self.gqry['state'] = 'disabled'
		return
	def cinptoggle(self,x):
		if x == 1:
			self.gqry['state'] = 'normal'
			self.gfile['state'] = 'normal'
		else:
			self.gqry['state'] = 'disabled'
			self.gfile['state'] = 'disabled'			
		return




# selects program to execute
	def selectProcess(self):
		self.clearpad()
		self.rsel['state'] = 'normal'
		ret = Ep.selectFile()

		if ret[0] == 2:
			messagebox.showinfo("Attention",ret[1])
			return
		self.runfile = ret[1]
		self.exts.set(os.path.basename(str(self.runfile)))

		data = Ep.readCode(self.runfile)

		if data[0] == 1:
			messagebox.showinfo("Attention",self.data[1])
			return	

		self.show(data[1])
		self.runtoggle(1)
		return


# run selected file
	def startExecution(self):
		query = self.tinp.get('1.0',T.END)
		if self.process is not None:
			self.stopExecution()

		ret = Ep.startExecution(self.runfile,query)
		if ret[0] == 100:
			self.process = ret[1]
			self.runtoggle(1)
		else:
			messagebox.showinfo("Attention",ret[1])
		return


# stop executing file
	def stopExecution(self):
		self.process.kill()
		self.process = None
		self.runtoggle(0)
		return


# save executing file
	def saveFile(self):
		backup = self.runfile
		try:
			data = self.show.get('1.0',T.END)
			with open(self.runfile,'w+',encoding='utf8') as f1:
				f1.write(data)
			self.runfile = backup
			messagebox.showinfo("Attention",'Saved')
		except:
			messagebox.showinfo('Attention','Error while Saving')
		return


# shows last assesment log		
	def logfun(self):
		self.clearpad()
		try:
			with open(r'supports/log.txt') as rd:
				data = rd.read()
			self.show(data)
		except Exception as e:
			messagebox.showinfo('Attention',e)
		return


# set previous
	def usePrevious(self):
		self.prev = True


# set guide
	def setGuide(self,i):
		for k in range(5):
			self.glbl[k]['text'] = self.guide[str(i)][str(k)]
		return
	

# clear all the guide labels
	def gclr(self):
		self.glbl[0]['text'] = self.glbl[1]['text'] = self.glbl[2]['text'] = self.glbl[3]['text'] = self.glbl[4]['text'] =   "" 
		return


# executes based on feature		
	def go(self,i):
		self.gclr()

		if i==0:
			reads = self.lshow.get('1.0',T.END) 
			if reads == "":
				messagebox.showinfo('Attention','No Data, Write Something.')
				self.gclr()
				return			
			query = self.tinp.get('1.0',T.END)
			self.glbl[0]['text'] = self.guide[str(i)]['5']
			if not self.prev:
				links = On.searchAPI(query)
			
			self.glbl[1]['text'] = self.guide[str(i)]['6']
			if not self.prev:
				On.saveScraped(links)
			self.glbl[2]['text'] = self.guide[str(i)]['7']
			similarity = On.checkPlagarism(reads)
			self.glbl[3]['text'] = self.guide[str(i)]['8']
			messagebox.showinfo("Similarity",str(similarity*100)+"%")
			self.glbl[4]['text'] = self.guide[str(i)]['9']
			self.prev = False

		elif i == 1:
			reads = self.lshow.get('1.0',T.END)
			if reads == "":
				messagebox.showinfo('Attention','No Data, Write Something.')
				self.gclr()
				return
			data1 = reads
			data2 = self.srcfile
			self.glbl[0]['text'] = self.guide[str(i)]['5']
			similars = Of.checkPlagarism(data1,data2)
			self.glbl[1]['text'] = self.guide[str(i)]['6']
			data = "MATCHED:\n\n"
			for s in similars['s']:
				data = data + '-' + s + '\n'
			self.show(data)
			messagebox.showinfo('Plagarism',str(similars['p']*100) + '% Similar')
			self.glbl[2]['text'] = self.guide[str(i)]['7']

		elif i == 2:
			pass

		elif i == 3:
			if reads == "":
				messagebox.showinfo('Attention','No Data, Write Something.')
				self.gclr()
				return
			self.glbl[0]['text'] = self.guide[str(i)]['5']
			sdata = Sm.summarizer(reads)
			self.clearpad()
			self.glbl[1]['text'] = self.guide[str(i)]['6']
			self.show(str(sdata))
			
		 
		elif i == 4:
			if self.reads == "":
				messagebox.showinfo('Attention','No Data, Restart Operation.')
				self.gclr()
				return
			self.openSelected()


		elif i == -1:
			messagebox.showinfo('Attention','Select Above feature to proceed.')
		return


	def onClick(self,i):
		self.dcrip.place(x=60,y=180)
		scrip=""
		self.gclr()
		self.CMD = i
		with open(r'supports/Guide.json') as f:
			self.guide = json.load(f)
		self.setGuide(i)
		if i==0:
			scrip = "This Feature will Perform Plagarism check Online using Internet Resources."
			self.basictoggle(1)
		elif i == 1:
			scrip = "This Feature will Perform Plagarism check using Selected Files locally."
			self.cinptoggle(1)
			self.basictoggle(1)
		elif i == 2:
			scrip = "This Feature will Perform Paraphrasing on given text data."
			self.basictoggle(1)
		elif i == 3:
			scrip = "This feature will provide Summary of given Assignment in short statements."
			self.cinptoggle(1)
		elif i == 4:
			scrip = "Have one cool idea. If I get time then sure implement it."
			self.basictoggle(1)
		elif i == 5:
			scrip = "This feature will let you Check code of File and also allows you to Execute/Modify it."
			self.rsel['state'] = "normal"
		self.dcrip['text'] = scrip
		return




# main frame creation
	root = T.Tk(className='Form')
	s1  = Labelframe(root,text='Option').place(x=30,y=60,width=1040,height=200)
	s = Labelframe(root,text='Execute')
	s.pack_forget()
	cls = T.Button(root,text='Close',command=root.destroy)
	
# making and loading other elements
	dsc = Labelframe(root,text='Assesment Input')
	sts = Labelframe(root,text='Guide and Assesment Status')
	lr = Labelframe(root,text='Files')
	lst = T.Listbox(root)
	rno=0
	reads=""
	synx=""
	query=""
	guide = ""
	process = None
	prev = False
	exts=T.StringVar(root)
	srcfile = None
	runfile = None
	dcrip = T.Label(root)
	brw = T.Button(root,text='Browse')
	sel = T.Button(root,text='Selcet')
	out = Labelframe(root,text='Text')
	lshow =  T.Text(root,width=78,height=33)
	tinp = T.Text(root,width=40,height=13)
	cpad = T.Button(root,text='Clear Pad')
	gqry = T.Button(root,text='Use Preious')
	gfile = T.Button(root,text='Source File')
	selfile = T.Label(root)
	runlbl = T.Label(root,textvariable=exts)
	rsel = T.Button(root,text='Select File')
	runcmd = T.Button(root,text='Run')
	runsv = T.Button(root,text='Save')
	title = ""
	logg = T.Button(root,text='Last Assesment Log')
	type=-1
	GO = T.Button(root,text='GO',fg='black',bg='white')
	glbl = list()
	runstop = T.Button(root,text='Stop')
	pid=None
	for i in range(5):
		glbl.append(T.Label(root))
		glbl[i].place(x=40,y=(630+(i*30)))
	CMD=-1
	bl=[]


	
	def __init__(self):
		print("Initializing..")
		self.root.geometry('500x500')
		self.root.title = 'Form'
		self.root.attributes('-fullscreen', True) 
		self.bl=["Online Plagarism Check", "Offline Plagarism Check","Paraphrase","Short Summary","-----","Run Code"]
		for i in range(len(self.bl)):
			b = T.Button(self.root,text=self.bl[i],bg='white',fg='black',command=lambda i=i:self.onClick(i))
			b.place(x=170*i+ 50,y=100,width=150,height=50)		
		
		self.brw.place(x=440,y=820,height=30,width=80)
		self.cls.place(x=1450,y=10,height=20,width=50)
		 
		self.dsc.place(x=30,y=290,width=350,height=300)
		self.sts.place(x=30,y=590,width=350,height=300)
		dscth = Style()
		dscth.theme_use('alt')
		self.lr.place(x=415,y=290,width=350,height=600)
		self.brw.configure(command=self.fillSelectionBox)
		self.sel.configure(command=self.openSelected)
		self.cpad.configure(command=self.clearpad)
		self.rsel.configure(command=self.selectProcess)
		self.runcmd.configure(command=self.startExecution)
		self.runsv.configure(command=self.saveFile)
		self.runstop.configure(command=self.stopExecution)
		self.runlbl.pack_forget()
		self.lst.place(x=427,y=310,width=325,height=500)
		self.sel.place(x=540,y=820,height=30,width=80)
		self.cpad.place(x = 640,y=820,height=30,width=100)
		self.out.place(x=800,y=290,width=650,height=600)
		self.lshow.place(x=810,y=310)
		self.tinp.place(x = 40,y=310)
		self.gqry.place(x=40,y=540,width=100,height=30)
		self.gqry.configure(command=self.usePrevious)
		self.runlbl.place(x=1110,y=100)
		self.gfile.place(x = 160,width=100,height=30,y=540)
		self.gfile.configure(command=self.secondFile)
		self.selfile.place(x=270,y=540)
		self.GO.place(x=900,y=180,height=50,width=150)
		self.GO.configure(command=lambda i=self.CMD:self.go(self.CMD))
		self.dcrip.pack_forget()
		self.rsel.pack_forget()
		self.s.place(x=1090,y=60,width=350,height=200)
		self.rsel.place(x = 1110,y=150,height=30,width=140)
		self.runstop.place(x = 1120+150,y=200,height=30,width=140)
		self.runcmd.place(x=1120+150,y=150,height=30,width=140)
		self.runsv.place(x=1110,y=200,height=30,width=140)
		self.runtoggle(0)
		self.basictoggle(0)
		self.cinptoggle(0)
		self.rsel['state'] = 'disabled'
		self.logg.configure(command=self.logfun)
		self.logg.place(x=40,y=800,height=30,width=150)
		
		

m=Mains()
m.root.mainloop()

