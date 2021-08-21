#!/usr/bin/python3

from modules import splits
import requests

urls = splits.urls_split

# test this pottential ssrf or no ?
class get():
	def __init__(self):
		pass

	def params(self, url):
		try:
			url = url.replace("FUZZ007", "collobrator")
			response = requests.get(url, verify=False, timeout=10)
			if "collobrator" in response.text:
				ssrfURL = url.replace("collobrator","[SSRF]")
				return ssrfURL
		except Exception as e:
			pass#print('error: ',e)	
