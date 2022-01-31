import requests
import urllib3
import re

response = requests.get("http://web.archive.org/cdx/search/cdx?url=*.burpcollaborator.net&output=txt&collapse=urlkey")

try:
	all_subs = re.findall(r"http?\:\/\/[A-Za-z0-9]*.burpcollaborator.net", response.text)
except Exception as error:
	print(error)


def as_list():
	for url in all_subs:
		try:
			response = requests.get(url, timeout=7)
			final_find = re.findall(r"\>[a-zA-Z0-9]{1,}", response.text)[0][1:]
			if (len(final_find) in [27, 34, 35, 36, 37, 38, 39, 40, 41]):
				return [url,final_find]
				break

		except Exception as error:
			pass



