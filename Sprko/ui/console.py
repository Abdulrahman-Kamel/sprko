#!/usr/bin/python3

import datetime
import os
from colorama import Fore
from Sprko.ui import arguments

arg = arguments.arg

banner_fmt = Fore.BLUE+"""  sSSs   .S_sSSs     .S_sSSs     .S    S.     sSSs_sSSs    
 d%%SP  .SS~YS%%b   .SS~YS%%b   .SS    SS.   d%%SP~YS%%b   
d%S'    S%S   `S%b  S%S   `S%b  S%S    S&S  d%S'     `S%b  
S%|     S%S    S%S  S%S    S%S  S%S    d*S  S%S       S%S  
S&S     S%S    d*S  S%S    d*S  S&S   .S*S  S&S       S&S  
Y&Ss    S&S   .S*S  S&S   .S*S  S&S_sdSSS   S&S       S&S  
`S&&S   S&S_sdSSS   S&S_sdSSS   S&S~YSSY%b  S&S       S&S  
  `S*S  S&S~YSSY    S&S~YSY%b   S&S    `S%  S&S       S&S  
   l*S  S*S         S*S   `S%b  S*S     S%  S*b       d*S  
  .S*P  S*S         S*S    S%S  S*S     S&  S*S.     .S*S  
sSS*S   S*S         S*S    S&S  S*S     S&   SSSbs_sdSSS   
YSS'    S*S         S*S    SSS  S*S     SS    YSSP~YSSY    
        SP          SP          SP                         
        Y           Y           Y            
\t  Develop by: Abdulrahman Kamel
\t  Github    : github.com/Abdulrahman-Kamel

"""+Fore.RESET  

class msg:
  
  def log(msg):
    if not arg.no_colors:
      return Fore.LIGHTGREEN_EX + "[LOG] " + Fore.RESET + msg
    else:
      return "[LOG] " + msg
    
  def info(msg):
    if not arg.no_colors:
      return Fore.LIGHTBLUE_EX + "[INFO] " + Fore.RESET + msg
    else:
      return "[INFO] " + msg


  def low(msg):
    if not arg.no_colors:
      return Fore.LIGHTGREEN_EX + "[LOW] " + Fore.RESET + msg
    else:
        return "[LOW] " + msg


  def medium(msg):
    if not arg.no_colors:
      return Fore.LIGHTYELLOW_EX + "[MEDIUM] " + Fore.RESET + msg
    else:
        return "[MEDIUM] " + msg



  def high(msg):
    if not arg.no_colors:
      return Fore.LIGHTMAGENTA_EX + "[HIGH] " + Fore.RESET + msg
    else:
        return "[HIGH] " + msg

  def critical(msg):
    if not arg.no_colors:
      return Fore.LIGHTRED_EX + "[CRITICAL] " + Fore.RESET + msg
    else:
        return "[CRITICAL] " + msg

  def Try(msg):
    if not arg.no_colors:
      return Fore.CYAN + "[TRY] " + Fore.RESET + msg
    else:
        return "[TRY] " + msg

  def interaction(msg):
    if not arg.no_colors:
      return Fore.CYAN + "[INTERACTION] " + Fore.RESET + msg
    else:
        return "[INTERACTION] " + msg

  def faield(msg):
    if not arg.no_colors:
      return Fore.LIGHTMAGENTA_EX + "[FAIELD] " + Fore.RESET + msg
    else:
        return "[FAIELD] " + msg

  def error(msg):
    if not arg.no_colors:
      return Fore.RED + "[ERROR] "+ Fore.RESET + msg
    else:
        return "[ERROR] " + msg

  def warning(msg):
    if not arg.no_colors:
      return Fore.YELLOW + "[WARNING] "+ Fore.RESET + msg
    else:
        return "[WARNING] " + msg

  def done(msg):
    if not arg.no_colors:
      return Fore.GREEN + "[SUCCESS] "+ Fore.RESET + msg
    else:
        return "[SUCCESS] " + msg

  def banner():
    return banner_fmt

  def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

  def exit():
    os._exit(1)


class Interpreter():
    def __init__(self):
        pass

    def CtrlZ(self):
        pass

    def CtrlC(self):
        pass


def status_code(statu):
  if str(statu)[0] == str(2):
    return Fore.LIGHTBLUE_EX + "("+str(statu)+")" + Fore.RESET

  if str(statu)[0] == str(3):
    return Fore.LIGHTGREEN_EX + "("+str(statu)+")" + Fore.RESET
    
  
  if str(statu)[0] == str(4):
    return Fore.LIGHTMAGENTA_EX + "("+str(statu)+")" + Fore.RESET
  
  if str(statu)[0] == str(5):
    return Fore.LIGHTRED_EX + "("+str(statu)+")" + Fore.RESET

def length(length):

  return Fore.CYAN+"["+str(len(length))+"KB]"+Fore.RESET

# print(Msg.info(' info hool'))
# print(Msg.low(' low hool'))
# print(Msg.medium(' medium hool'))
# print(Msg.high(' high hool'))
# print(Msg.critical(' critical hool'))
# print(Msg.Try(' Try hool'))
# print(Msg.interaction(' interaction hool'))
# print(Msg.faield(' faield hool'))


