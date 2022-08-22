import os 
from os import environ as env, system as sys, getcwd

from requests import get 
from selenium import webdriver
from colorama import Fore
from time import sleep
from pystyle import Anime, Center, Colors, Colorate, System
from pypresence import Presence
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes
from json import load

#=========================== basic vars ===========================
#colors 
y = Fore.MAGENTA
b = Fore.LIGHTBLACK_EX
w = Fore.LIGHTWHITE_EX

program_file = env["ProgramW6432"]
program_file_2 = env["ProgramFiles"]
program_file_x86 = env["ProgramFiles(x86)"]


#=========================== banners vars ===========================

banner_pystyle= """
███████╗██╗   ██╗███████╗██╗███╗   ██╗████████╗
██╔════╝██║   ██║██╔════╝██║████╗  ██║╚══██╔══╝
███████╗██║   ██║███████╗██║██╔██╗ ██║   ██║   
╚════██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
███████║╚██████╔╝███████║██║██║ ╚████║   ██║   
╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   """
banner= f"""
███████╗██╗   ██╗███████╗██╗███╗   ██╗████████╗
██╔════╝██║   ██║██╔════╝██║████╗  ██║╚══██╔══╝
███████╗██║   ██║███████╗██║██╔██╗ ██║   ██║   
╚════██║██║   ██║╚════██║██║██║╚██╗██║   ██║   
███████║╚██████╔╝███████║██║██║ ╚████║   ██║   
╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
{b}============ github.com/crashixx =============\n""".replace('█', f'{b}█{y}')

#=========================== basic defs ===========================

def rpc():
    try:
        rpc = Presence("713734159574630420")
        rpc.connect()
        rpc.update(state="by crashixx",details=f"OSINT tool",large_image="logo_resize_")
    except:
        pass

def clear():
    sys("cls")


    