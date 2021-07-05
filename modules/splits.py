#!/usr/bin/python3

import exurl
from Sprko.ui import arguments
from modules import readData, Filter

dataFromUser = readData.urls()
urls = Filter.urlsParam(dataFromUser)
urls_split = exurl.split_urls(urls, "FUZZ007")