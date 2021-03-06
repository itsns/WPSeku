#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# WPSeku - Wordpress Security Scanner
# by Momo Outaadi (m4ll0k)

from re import search,findall,I
from lib.request import * 
from lib.printer import *
from lib.check import *
from lib.readfile import *

class wprobots(Request):
	def __init__(self,url,data,kwargs):
		self.url = url 
		self.data = data
		self.kwargs = kwargs
		Request.__init__(self,kwargs)

	def run(self):
		if self.kwargs['verbose'] is True:
			info('Checking robots paths...')
		url = Path(self.url,'robots.txt')
		resp = self.send(url=url,method="GET")
		if resp.status_code == 200 and resp.content != ("" or None):
			if resp.url == url:
				plus('Robots was found at: %s'%resp.url)
				print("-"*40+"\n%s\n"%resp.content.decode('utf-8')+"-"*40)