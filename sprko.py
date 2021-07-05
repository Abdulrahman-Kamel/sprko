#!/usr/bin/python3

from Sprko.ui import arguments, console
from modules import install, splits
from Sprko.ui import arguments, console
from Sprko.core import verify, threads
from Sprko.core.main import ssrf as main
from Sprko.core.exploit import responseVerify as exploit
# from modules import readData, sender

# Auto install require packages
install.packages()

# print banner
print(console.banner_fmt)

if __name__ == '__main__':
	main()