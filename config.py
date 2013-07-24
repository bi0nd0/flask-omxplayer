# -*- coding: utf-8 -*-

local_movie='media'
online_movie='http://192.168.1.100:8888/'
movie_type = ['mp4', 'avi', 'mp3', 'flv']
port=5000
omxoptions = "-o hdmi" 
player='omxplayer'


class BaseConfig(object):
	DEBUG = True

	SECRET_KEY = 'development key'
	USERNAME = 'admin'
	PASSWORD = 'admin'

	RECAPTCHA_USE_SSL = False
	RECAPTCHA_PUBLIC_KEY = '6LdTAOISAAAAAG42VqD3hIeTEM78UaU4t2Gt6Eja'
	RECAPTCHA_PRIVATE_KEY = '6LdTAOISAAAAALP6OCYrhgNtM9TYCE-S4-WM-5bj'
	RECAPTCHA_OPTIONS = {'theme': 'white'}

	CACHE_TYPE = 'simple'
	
class DefaultConfig(BaseConfig):
	pass
	