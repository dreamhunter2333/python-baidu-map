# -*- coding: utf-8 -*-

__author__ = 'jinmu333'

from tkinter import *
from multiprocessing import Process
import tkinter.messagebox as messagebox
import urllib,hashlib
import random
import requests,sys
import requests
import urllib.parse
import urllib.request
import urllib,hashlib
import random
import json

print("你好，这是经纬度查询软件")

root = Tk()
root.title("经纬度查询 by jinmu333")
root.geometry('400x500')                 #是x 不是*
root.resizable(width=True, height=True) #宽不可变, 高可变,默认为True
l = Label(root, text="更多软件加qq2544236134", font=("Arial", 9), width=20)
l.pack(side=BOTTOM)    
t = Text()
t.pack()
t.insert('1.0', "此处显示历史经纬度查询记录\n")
var = StringVar()
e = Entry(root, textvariable = var)
var.set('此处显示最新输出内容')
e.pack()
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.bind('<Key-Return>',self. hello)
		self.nameInput.pack()
		self.alertButton = Button(self, text='查询地址', command=self.hello,width = 20,height = 2,bd = 2)
		self.alertButton.pack()
    
	def hello(self,event):
		s = self.nameInput.get() or '北京'
		
		address = s

		data = urllib.parse.urlencode({'address': s, 'output': 'json','ak':'FrMYLYzOeELKZ3kfWvBc6rDNsUik788s'})
		response = urllib.request.urlopen('http://api.map.baidu.com/geocoder/v2/?%s' % data)
		  
		html = response.read()
		data = html.decode('utf-8')
		print(data)

		jsonData = json.loads(data)
		lat=jsonData['result']['location']['lat']
		lng =jsonData['result']['location']['lng']
		level=jsonData['result']['level']
		var.set('请在下方键入查询地点')
		t.insert('1.0', "-------------------------------------------------------\n")
		t.insert('1.0', "          类型:%s\n" %level)
		t.insert('1.0', "          经度=%f\n" %lng)
		t.insert('1.0', "查询结果: 纬度=%f\n" %lat)
		t.insert('1.0', "查询地点: %s\n" %s)
app = Application()
    
# 主消息循环:
app.mainloop()