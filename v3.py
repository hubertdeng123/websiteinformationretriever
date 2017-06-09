#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Hubert Deng

from collections import namedtuple
from bs4 import BeautifulSoup
import urllib2, sys, datetime, webbrowser
from Tkinter import *
import Tkinter as tk
from ttk import *

Websites=[]
term=""
stuff=""

def store(date, url, title, name):
	Info=namedtuple("Info", "date url title seconds name temp")
	count=1
	num=[]
	curr=total=0
	temp=""
	multiplier=[31556926, 2629744, 86400, 3600, 60, 1]
	for i in range(0, len(date)):
		try: 
			int(date[i])
			temp+=date[i]
		except:
			temp+="-"
			count+=1
	temp+="-"
	while temp[len(temp)-1]==temp[len(temp)-2]=="-":
		temp=temp[:len(temp)-1]
		count-=1
	while temp[0]=="-":
		temp=temp[1:]
		count-=1
	for i in range(0, count):
		place=""
		while temp[curr]!="-":
			place+=temp[curr]
			curr+=1
		num.append(int(place))
		curr+=1
	for i in range(0, count):
		total+=num[i]*multiplier[i]
	storedInfo=Info(date, url, title, total, name, temp)
	return storedInfo

def sort(list):
	sorted=False
	while not sorted:
		sorted=True
		for i in range(0, len(list)-1):
			if getattr(list[i], "seconds")<getattr(list[i+1], "seconds"):
				sorted=False
				temp=list[i+1]
				list[i+1]=list[i]
				list[i]=temp
	return list	
	
def getWebsites():
	try:
		page=urllib2.urlopen("http://zhannei.baidu.com/cse/search?q=%s&s=1990107715198738414"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('a',{'cpos':'title'})
		info=soup.find_all('div',{'class':'c-abstract'})
		date=soup.find_all('span',{'class':'c-showurl'})
		for i in range(0, len(titles)):
			Websites.append(store(date[i].text[date[i].text.rfind(" ")+1:], titles[i]['href'], titles[i].text, u"\u4e1c\u5357\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://www.dnkb.com.cn/index.php?m=search&c=index&a=init&siteid=1&typeid=1&q=%s"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('span', {"class":"title"})
		date=soup.find_all('span', {"class":"time"})
		for i in range(0, len(titles)):
			place=str(titles[i])
			place=BeautifulSoup(place, "html.parser")
			place2=place.find('a')
			Websites.append(store(date[i].text[date[i].text.find(u"\uff1a")+1:], "http://www.dnkb.com.cn"+place2['href'], place2.text, u"\u4e1c\u5feb\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://zhannei.baidu.com/cse/search?s=6994307491708932867&entry=1&q=%s"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('a',{'cpos':'title'})
		info=soup.find_all('div',{'class':'c-abstract'})
		date=soup.find_all('span',{'class':'c-showurl'})
		for i in range(0, len(titles)):
			Websites.append(store(date[i].text[date[i].text.rfind(" ")+1:], titles[i]['href'], titles[i].text, u"\u6d77\u90fd\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://zhannei.baidu.com/cse/search?s=7892531895481577194&entry=1&q=%s"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('a',{'cpos':'title'})
		info=soup.find_all('div',{'class':'c-abstract'})
		date=soup.find_all('span',{'class':'c-showurl'})
		for i in range(0, len(titles)):
			Websites.append(store(date[i].text[date[i].text.rfind(" ")+1:], titles[i]['href'], titles[i].text, u"\u798f\u5dde\u65b0\u95fb\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://zhannei.baidu.com/cse/search?entry=1&s=6497631107033654394&q=%s"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('a',{'cpos':'title'})
		info=soup.find_all('div',{'class':'c-abstract'})
		date=soup.find_all('span',{'class':'c-showurl'})
		for i in range(0, len(titles)):
			Websites.append(store(date[i].text[date[i].text.rfind(" ")+1:], titles[i]['href'], titles[i].text, u"\u95fd\u5357\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://sou.chinanews.com.cn/search.do?q=%s"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('li', {"class":"news_title"})
		info=soup.find_all('li', {"class":"news_content"})
		date=soup.find_all('li', {"class":"news_other"})
		for i in range(0, len(titles)):
			place=str(titles[i])
			place=BeautifulSoup(place, "html.parser")
			place2=place.find('a')
			Websites.append(store(date[i].text[date[i].text.rfind(" ")-10:date[i].text.rfind(" ")+9], place2['href'], place2.text, u"\u4e2d\u56fd\u65b0\u95fb\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://search.sina.com.cn/?range=all&c=news&from=dfz&q=%s"%stuff)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('h2')
		date=soup.find_all('span', {"class":"fgray_time"})
		info=soup.find_all('p', {"class":"content"})
		for i in range(0, len(titles)):
			place=str(titles[i])
			place=BeautifulSoup(place, "html.parser")
			place2=place.find('a')
			Websites.append(store(date[i].text[len(date[i].text)-19:], place2['href'], place2.text, u"\u65b0\u6d6a\u798f\u5efa"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://www.sogou.com/tx?site=fj.qq.com&query=%s&hdq=sogou-wsse-b58ac8403eb9cf17-0050&sourceid=sugg&idx=f"%stuff)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('h3')
		for i in range(1, 10):
			place=str(titles[i])
			place=BeautifulSoup(place, "html.parser")
			place2=place.find('a')	
			date=soup.find('cite', {"id":"cacheresult_info_"+str(i-1)})
			info=soup.find('div', {"id":"cacheresult_summary_"+str(i-1)})
			Websites.append(store(date.text[date.text.rfind(u"\xa0")+1:], place2['href'], place2.text, u"\u5927\u95fd\u7f51\u65b0\u95fb"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://zhannei.baidu.com/cse/search?q=%s&p=0&s=16378496155419916178&entry=1&area=2"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('a',{'cpos':'title'})
		info=soup.find_all('div',{'class':'c-abstract'})
		date=soup.find_all('span',{'class':'c-showurl'})
		for i in range(0, len(titles)):
			Websites.append(store(date[i].text[date[i].text.rfind(" ")+1:], titles[i]['href'], titles[i].text, u"\u51e4\u51f0\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://bbs.163.com/bbs/search.do?boardid=photo&orderbytime=n&q=%s&searchType=body&searchRan=bbs"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('h3')
		date=soup.find_all('span', {"class":"date"})
		info=soup.find_all('div', {"class":"textA"})
		for i in range(0, len(titles)):
			place=str(titles[i])
			place=BeautifulSoup(place, "html.parser")
			place2=place.find('a')
			Websites.append(store(date[i].text[date[i].text.rfind("[")+1:len(date[i].text)-1], place2['href'], place2.text, u"\u7f51\u6613"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://info.search.news.cn/result.jspa?ss=2&t=1&t1=0&rp=10&np=1&n1=%s"%stuff)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('span', {"class":"style1d"})
		date=soup.find_all('span', {"class":"style2a"})
		info=soup.find_all('span', {"class":"cc"})
		for i in range(len(titles)):
			place=str(titles[i])
			place=BeautifulSoup(place, "html.parser")
			place2=place.find('a')
			Websites.append(store(date[i].text[date[i].text.find(" ")+2:], place2['href'], place2.text, u"\u65b0\u534e\u7f51"))
	except:
		pass
	try:
		page=urllib2.urlopen("http://203.192.8.57/was5/web/search?sw=%s&channelid=282612&searchword=%E7%BD%97%E6%BA%90&prepage=40"%term)
		soup=BeautifulSoup(page.read(), "html.parser")
		titles=soup.find_all('a',{'target':'_blank'})
		date=soup.find_all('span')
		for i in range(0, len(titles)):
			Websites.append(store(date[i].text, titles[i]['href'], titles[i].text, u"\u7ecf\u6d4e\u53c2\u8003\u7f51"))
	except:
		pass
def click1(event, url, tag_name):
	res=event.widget
	res.tag_config(tag_name, background='red')
	res.update_idletasks()
	webbrowser.open_new(url)
	res.tag_config(tag_name, background='white')
	res.update_idletasks()
	
def b1(storedInfo):
	global Websites
	Websites=[]
	getWebsites()
	Websites=sort(Websites)
	storedInfo.delete(1.0, END)
	now=datetime.datetime.now()
	time=[int(now.year), int(now.month), int(now.day), int(now.hour), int(now.minute), int(now.second)]
	multiplier=[31556926, 2629744, 86400, 3600, 60, 1]
	temporary=0	
	for i in range(0, 6):
		temporary+=multiplier[i]*time[i]
	for i in range(0, len(Websites)):
		if temporary-getattr(Websites[i], "seconds")<=86400:
			url=getattr(Websites[i], "url")
			tag_name="link"+str(i)
			storedInfo.insert(END, getattr(Websites[i], "name")+"\n")
			storedInfo.insert(END, getattr(Websites[i], "title")+"\n")
			callback=(lambda event, url=url, tag_name=tag_name:click1(event, url, tag_name))
			storedInfo.tag_bind(tag_name, "<Button-1>", callback)
			storedInfo.insert(END, getattr(Websites[i], "url")+"\n", (tag_name,))
			storedInfo.insert(END, getattr(Websites[i], "date")+"\n"+"\n")
def b2(storedInfo):
	global Websites
	Websites=[]
	getWebsites()
	Websites=sort(Websites)
	storedInfo.delete(1.0, END)
	now=datetime.datetime.now()
	time=[int(now.year), int(now.month), int(now.day), int(now.hour), int(now.minute), int(now.second)]
	multiplier=[31556926, 2629744, 86400, 3600, 60, 1]
	temporary=0	
	for i in range(0, 6):
		temporary+=multiplier[i]*time[i]
	for i in range(0, len(Websites)):
		if temporary-getattr(Websites[i], "seconds")<=259200:
			url=getattr(Websites[i], "url")
			tag_name="link"+str(i)
			storedInfo.insert(END, getattr(Websites[i], "name")+"\n")
			storedInfo.insert(END, getattr(Websites[i], "title")+"\n")
			callback=(lambda event, url=url, tag_name=tag_name:click1(event, url, tag_name))
			storedInfo.tag_bind(tag_name, "<Button-1>", callback)
			storedInfo.insert(END, getattr(Websites[i], "url")+"\n", (tag_name,))
			storedInfo.insert(END, getattr(Websites[i], "date")+"\n"+"\n")

def b3(storedInfo):
	global Websites
	Websites=[]
	getWebsites()
	Websites=sort(Websites)
	storedInfo.delete(1.0, END)
	now=datetime.datetime.now()
	time=[int(now.year), int(now.month), int(now.day), int(now.hour), int(now.minute), int(now.second)]
	multiplier=[31556926, 2629744, 86400, 3600, 60, 1]
	temporary=0	
	for i in range(0, 6):
		temporary+=multiplier[i]*time[i]
	for i in range(0, len(Websites)):
		if temporary-getattr(Websites[i], "seconds")<=604800:
			url=getattr(Websites[i], "url")
			tag_name="link"+str(i)
			storedInfo.insert(END, getattr(Websites[i], "name")+"\n")
			storedInfo.insert(END, getattr(Websites[i], "title")+"\n")
			callback=(lambda event, url=url, tag_name=tag_name:click1(event, url, tag_name))
			storedInfo.tag_bind(tag_name, "<Button-1>", callback)
			storedInfo.insert(END, getattr(Websites[i], "url")+"\n", (tag_name,))
			storedInfo.insert(END, getattr(Websites[i], "date")+"\n"+"\n")
def b4(storedInfo):
	global Websites
	Websites=[]
	getWebsites()
	Websites=sort(Websites)	
	storedInfo.delete(1.0, END)
	now=datetime.datetime.now()
	time=[int(now.year), int(now.month), int(now.day), int(now.hour), int(now.minute), int(now.second)]
	multiplier=[31556926, 2629744, 86400, 3600, 60, 1]
	temporary=0	
	for i in range(0, 6):
		temporary+=multiplier[i]*time[i]
	for i in range(0, len(Websites)):
			url=getattr(Websites[i], "url")
			tag_name="link"+str(i)
			storedInfo.insert(END, getattr(Websites[i], "name")+"\n")
			storedInfo.insert(END, getattr(Websites[i], "title")+"\n")
			callback=(lambda event, url=url, tag_name=tag_name:click1(event, url, tag_name))
			storedInfo.tag_bind(tag_name, "<Button-1>", callback)
			storedInfo.insert(END, getattr(Websites[i], "url")+"\n", (tag_name,))
			storedInfo.insert(END, getattr(Websites[i], "date")+"\n"+"\n")

class Checkbar(Frame):
	def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
		Frame.__init__(self, parent)
		self.vars=[]
		var=IntVar()
		for i in range(len(picks)):
			chk=Radiobutton(self, text=picks[i], variable=var, value=i+1)
			chk.pack(side=side, anchor=anchor, expand=YES)
			self.vars.append(var)
	def state(self):
		return map((lambda var: var.get()), self.vars)

		
def allstates(): 
	return list(checklist.state())

def chooser():
	global term
	global stuff
	term=e.get().encode("utf8")
	stuff=e.get().encode("gb2312")
	choice=allstates()
	if choice[0]==1:
		b1(text)
	elif choice[0]==2:
		b2(text)
	elif choice[0]==3:
		b3(text)
	elif choice[0]==4:
		b4(text)

root=Tk()
root.title("Website Information Retriever, Created by Hubert Deng")
v=StringVar()
e=Entry(root, textvariable=v)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text=Text(root, yscrollcommand=scrollbar.set, height=54, width=200)
Label(text='Keyword').pack()
e.pack()
checklist=Checkbar(root, [u'24\u5c0f\u65f6\u4e4b\u5185', u'\u6700\u8fd1\u4e09\u5929', u'\u6700\u8fd1\u4e00\u4e2a\u661f\u671f', u'\u5168\u90e8'+"   "])
checklist.pack()
Button(root, text='Search', command=chooser).pack()
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
text.pack(anchor=NW)
root.mainloop()
		