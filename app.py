# -*- coding: utf-8 -*-

from flask import request, flash, g, session
from flask import render_template, redirect, url_for
import omxplayer
import urllib

from config import DefaultConfig, local_movie, online_movie, omxoptions
from init_app import create_app

from extensions import get_online_files, get_local_files

app = create_app(DefaultConfig)

player = None
playing = None

@app.route('/')
def index():
	print str(get_online_files())
	return render_template('index.html', files=get_online_files())

@app.route('/player', methods=['POST', 'GET'])
def web_player():
	print request.args, 111
	print exec_command(request.args['c'])
	return 'waaa'
	
def exec_command(command):
	global player,playing
	if command == 'pause':
		player.toggle_pause()

	elif command == 'play':
		if player != None and player.is_running():
			exec_command('quit')
		if request.args['online'] =='1':
			path = online_movie + urllib.quote(request.args['file'])
		else:
			
			ml = urllib.unquote(movie_location)
			fil = urllib.unquote(request.query.file)
			path = ml+fil
			if check_input(ml,fil) == False:
				return None
		
		print path, 11221212
		player = omxplayer.OMXPlayer(path, omxoptions,start_playback=True, do_dict=True)
		playing = path
		print 'Playing: '+str(ml+fil)

	elif command == 'ahead':
		player.skip_ahead()

	elif command == 'back':
		player.skip_back()

	elif command == 'quit':
		player.stop()
		playing = None
		player = None
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)