#!/usr/bin/python3

import yaml as yamlModule
from Sprko.ui import arguments

arg = arguments.arg

# read data from file as list :: additional arg.url to list
def urls():
	data = []
	if arg.urls:
		for line in open(arg.urls, 'r'):
			data.append(line.strip())
		open(arg.urls, 'r').close()
		
	if arg.url:
		data.append(arg.url)

	return data

def yaml(path):
	of = open(path)
	parser = yamlModule.load(of, Loader=yamlModule.FullLoader)
	return parser

def sender(data):
	return yaml('config/sender.yaml')[data]