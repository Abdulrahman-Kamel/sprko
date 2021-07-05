#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40))
parser.add_argument("-u", "--url", 		help="One url to testing", metavar="")
parser.add_argument("-U", "--urls", 		help="File contains many urls to testing", metavar="")
parser.add_argument("-l", "--logs", 		help="Show all request url with status code", action="store_true")
parser.add_argument("-b", "--bar", 		help="Enable the progress bar", action="store_true")
parser.add_argument("-r", "--report", 		help="Report to [slack|telegram], look to config/sender.yaml", action="store_true")

#parser.add_argument("-header", 		help="Addtional header in every request", metavar="")
#parser.add_argument("-r", "--request-file", 		help="Improve request file alike burp repeter", metavar="")
parser.add_argument("-n", "--no-exploit", 	help="No exploit ssrf | extract metafiles data", action="store_true")
parser.add_argument("-t", "--threads", 	help="Thread number to MultiProccess", metavar="")
parser.add_argument("-s", "--silent", 		help="Thread number to MultiProccess", action="store_true")
parser.add_argument("-c", "--no-colors", 	help="Thread number to MultiProccess", action="store_true")
parser.add_argument("-S", "--sleep",  		help="Sleep after every request", metavar="")
parser.add_argument("-o", "--output", 		help="Save output to results", metavar="")

arg = parser.parse_args()
max_threads = int(arg.threads) if arg.threads else int(30)
max_sleep   = int(arg.sleep) if arg.sleep else int(0.00001)
# header 		= dict(arg.header) if arg.header else None

