#!/usr/bin/python3

from modules import readData
from re import match

def urlsParam(old):
	urls_list = []
	regex_url_with_param = r"^(http|https).*\=.*"
	for url in old:
		matchTrue = match(regex_url_with_param, url)
		if matchTrue:
			urls_list.append(url)
	return urls_list