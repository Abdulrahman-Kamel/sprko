#!/usr/bin/python3

import importlib
from colorama import Fore
import pip

class packages():
	def __init__(self):
		self.pkg('requests')
		self.pkg('argparse')
		self.pkg('exurl')
		self.pkg('urllib3')
		self.pkg('concurrent')
		self.pkg('urllib')
		self.pkg('re')
		self.pkg('colorama')
		self.pkg('datetime')

	def checkPackage(self, package):
		get_pkg_path   = importlib.util.find_spec(package)
		check_found = get_pkg_path is not None
		return check_found

	def pkg(self, package):
		pkg = self.checkPackage(package)
		if pkg == False:
			print(Fore.RED+ "Install Python Package "+Fore.RESET+Fore.GREEN+"["+package+"]"+Fore.RESET)
			pip.main(['install', package])

	def downloadProxies(self):
		pass