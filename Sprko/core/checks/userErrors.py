#!/usr/bin/python3

from Sprko.ui import arguments, console
from sys import exit

arg = arguments.arg
msg = console.msg

def inputs():
	errors = []
	
	# check on urls argument
	if not arg.urls:
		errors.append('urls')
		print(msg.error("-u, --urls Required agument"))
		exit(1)
