#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep, environ
import rxv
import json

PORT_NUMBER = 8080

receiver = rxv.RXV("http://"+environ['AMP_IP']+":80/YamahaRemoteControl/ctrl", "AMP")
print(receiver)

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/on":
			receiver.on = True
                if self.path=="/off":
                        receiver.on = False
		self.send_response(200)
                self.send_header("Content-type", "application/json")
	        self.end_headers()
		response = receiver.basic_status.__dict__
                playStatus = receiver.play_status()
                if playStatus is not None:
                        response.update(playStatus.__dict__)
		self.wfile.write(json.dumps(response))
		return
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	
