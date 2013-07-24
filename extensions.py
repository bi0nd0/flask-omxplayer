# -*- coding: utf-8 -*-
import os, sys
import re
import urllib

from flask import request, render_template

from config import local_movie, online_movie, movie_type

def local_files(dr=''):
	foders = []
	files = []
	for i in os.listdir(urllib.unquote(local_movie+'/'+dr)):
		if os.path.isdir(urllib.unquote(local_movie+'/'+dr+'/'+i)):
			foders.append([urllib.unquote(i), i])
		else:
			files.append([urllib.unquote(i), i])


def get_online_files():
	movie = []
	try:
		f = urllib.urlopen(online_movie).read()
	except:
		raise NotImplementedError
	files =  re.findall( r'<a href="(.+?)">', f)
	for f in files:
		if f.split('.')[-1] in movie_type:
			print f, 1212
			print  urllib.unquote(f), 2323
			print  urllib.unquote(f).decode('utf-8'), 2323444
			movie.append(urllib.unquote(f).decode('utf-8'))
	return movie
	
def get_local_files():
	
	if request.query.dr == None:
		dr = ''
	else:
		dr = urllib.unquote(request.query.dr)
		
	d = []
	f = []
	for i in os.listdir(urllib.unquote(local_movie+'/'+dr)):
		if os.path.isdir(urllib.unquote(local_movie+'/'+dr+"/"+i)):
			d.append([urllib.unquote(i),i])
		else:
			f.append([urllib.unquote(i),i])
	# f.sort(comparator)
	# d.sort(comparator)
	return render_template('files_list', dir_list=d,file_list=f,dr=urllib.unquote(dr))

	
	
	