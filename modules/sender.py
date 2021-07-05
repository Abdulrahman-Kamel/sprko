#!/usr/bin/python3

from Sprko.ui import arguments, console
from requests import post as sendPostRequest
from urllib3 import disable_warnings
from modules import readData

# skip ssl error
disable_warnings()
msg = console.msg

telegram_config    = readData.sender('telegram')
telegram_bot_api   = readData.sender('telegram')['bot_api']
telegram_chat_id   = readData.sender('telegram')['chat_id']

slack_config   	  = readData.sender('slack')
slack_secret   	  = readData.sender('slack')['secret']

class contact():

	def telegram(telegram_bot, telegram_chat, message):
		if telegram_config['enable'] != False:

			telegram_api_url = "https://api.telegram.org/bot{}/sendMessage".format(str(telegram_bot))
			post_data    	 = {"chat_id":str(telegram_chat), "text":str(message)}
			
			try:
				response = sendPostRequest(telegram_api_url, data=post_data, verify=False)
				if str(response.status_code)[0] in ("3","4","5"):
					print(msg.faield("Telegram send notification"))
			except Exception as e:
				of = open("log/errors.log", "a+")
				wf = of.writelines("error sender.py [telegram]: "+url+": "+str(e)+"\n")
				cf = of.close()

				
		
	def slack(slack_secret, message):
		if slack_config['enable'] != False:

			slack_api_url = "https://hooks.slack.com/services/{}".format(slack_secret)
			json_data     = {"text":str(message)}

			try:
				response = sendPostRequest(slack_api_url, json=json_data, verify=False)
				if str(response)[0] in ("3","4","5"):
					print(msg.faield("Slack send notification"))
			except Exception as e:
				of = open("log/errors.log", "a+")
				wf = of.writelines("error sender.py: [slack]"+url+": "+str(e)+"\n")
				cf = of.close()
