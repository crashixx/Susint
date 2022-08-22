from utils.plugin.susint_base import *
from utils.mailchecker.mail_checker import *
from utils.anuarychecker.anuarychecker import *
from utils.socialchecker.socialcheker import *
from utils.websitechecker.websitechecker import *

#=========================== rich prescence initialize ===========================
rpc()
#=========================== firefox checker ===========================

if os.path.exists(f"{program_file}\\Mozilla Firefox\\firefox.exe") == True:
    firefox_path = f"{program_file}\\Mozilla Firefox\\firefox.exe" 
elif os.path.exists(f"{program_file_x86}\\Mozilla Firefox\\firefox.exe") == True:
    firefox_path = f"{program_file_x86}\\Mozilla Firefox\\firefox.exe"
elif os.path.exists(f"{program_file_2}\\Mozilla Firefox\\firefox.exe") == True:
    firefox_path = f"{program_file_2}\\Mozilla Firefox\\firefox.exe"
else:
    clear()
    print(banner)
    firefox_path = input(f"{y}[{w}#{y}]{w}Le navigateur firefox n'est pas detecté !...\n{y}[{w}#{y}]{w}Est-il installé?\n=~=~=\n{y}[{w}#{y}]{w}Si oui entrez le chemin d'acces ici:\n>>>")
    if firefox_path == "":
        exit()
    else:
        pass

#=========================== api keys scraper ===========================

with open("api_keys.json", "r") as f:
    api_keys = load(f)

#=========================== user menu ===========================

sys("title Susint v1.0 - by crashixx")
Anime.Fade(Center.Center(banner_pystyle), Colors.purple_to_blue, Colorate.Vertical, interval=1.5, enter=True)

clear()
print(banner)
print(f"""{y}[{b}+{y}]{w} Options:

{y}[{w}01{y}]{w} Search by firstname & name                
{y}[{w}02{y}]{w} Search by username
=====""")

choice = input(f"""\n{y}[{b}#{y}]{w} Choix: """)
if choice == str("1"):
    clear()
    print(banner)
    firstname = input(f"{y}[{w}#{y}]{w}Enter your firstname:\n>>>")
    clear()
    print(banner)
    name = input(f"{y}[{w}#{y}]{w}Entrer your familyname:\n>>>")
if choice == str("2"):
    clear()
    print(banner)
    username = input(f"{y}[{w}#{y}]{w}Enter your username:\n>>>")

clear()
print(banner)
print(f"{y}[{w}INFO{y}]{w} Search in progress....")


#=========================== driver setup ===========================

opts = webdriver.FirefoxOptions()
opts.headless = True
opts.binary = firefox_path
driver = webdriver.Firefox(options=opts, executable_path=r'geckodriver.exe')
SetFileAttributes(f"{getcwd()}\\geckodriver.log", FILE_ATTRIBUTE_HIDDEN)

#=========================== possible username creator ===========================

#firstname & name
if choice == str("1"):
    usr1 = f"{firstname}.{name}"
    usr2= f"{name}.{firstname}"
    usr3 = f"{firstname}_{name}"
    usr4= f"{name}_{firstname}"
    usr5 = f"{firstname}-{name}"
    usr6= f"{name}-{firstname}"
    usr7= f"{name}{firstname}".replace(" ", "")
    usr8= f"{firstname}{name}".replace(" ", "")
elif choice == str("2"):
    usr1 = f"{username}"
    usr2= f"_{username}"
    usr3 = f"{username}_"
    usr4= f"_{username}_"
    usr5 = f"{username}"
    usr6= f"xxx{username}xxx"
    usr7= f"_-{username}-_"
    usr7= f"-_{username}_-"
    usr8= f"{username}"*2

#=========================== email reserch per fisrtname and secondname ===========================

valid_mails = []

mail_checker(usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8, api_keys, valid_mails)

#=========================== adress & telf scraper ===========================

adress = []
nums = []
if choice == str("1"):
    usr = f"{firstname}+{name}"
else:
    usr = f"{username}"

anuarychecker(driver, adress, nums, usr)

#=========================== social scraper ===========================

socials = ["https://instagram.com/", "https://www.facebook.com/", "https://www.twitch.tv/", "https://twitter.com/","https://pr0gramm.com/user/", "https://www.npmjs.com/~", 
"https://note.com/", "http://www.authorstream.com/", "https://youpic.com/photographer/", "https://www.virustotal.com/ui/users/", "https://vimeo.com/", "https://tryhackme.com/p/", 
"https://tenor.com/users/", "https://open.spotify.com/user/", "https://sourceforge.net/u/", "https://soundcloud.com/", "https://www.smule.com/", "https://scratch.mit.edu/users/", 
"https://replit.com/@","https://raidforums.com/User-", "https://pypi.org/user/", "https://www.pinterest.com/", "https://onlyfans.com/", "https://imgur.com/user/", 
"https://forum.hackthebox.eu/profile/", "https://www.github.com/"]
working_socials = []

socialchecker(socials, working_socials, usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8)

#=========================== website checker ===========================

start_url = ["http://", "https://"]
domains = [".fr", ".es", ".ma", ".uk", ".xyz", ".ga", ".ru", ".com", ".online",
".live", ".store", ".tech", ".site", ".website"]
working_domains = []

websitechecker(start_url, domains, working_domains, usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8)

#=========================== final output ===========================

adress_phone = []

clear()
print(banner)

#mails
print(f"{y}[{w}>{y}]{w} {len(valid_mails)} valid mail(s) found :\n")
for x in valid_mails:
    print(f"{y}[{w}MAIL{y}]{w} {x}")

#adress & phone
for x in range(len(adress)):
    adress_phone.append(f"{adress[x]}\n{nums[x]}")
print(f"\n=====\n{y}[{w}>{y}]{w} {len(adress)} valid adress & phone(s) found :\n")
for x in adress_phone:
    print(f"{w}↓ {y}[{w}ADRESS & PHONE{y}]{w} ↓\n{x}")

#socials
print(f"\n=====\n{y}[{w}>{y}]{w} {len(working_socials)} valid social(s) found :\n")
for x in working_socials:
    print(f"{y}[{w}SOCIAL{y}]{w} {x}")

#website
print(f"\n=====\n{y}[{w}>{y}]{w} {len(working_domains)} valid website(s) found :\n")
for x in working_domains:
    print(f"{y}[{w}WEBSITE{y}]{w} {x}")

input(f"\n=====\n{y}[{w}LOG{y}]{w} Operation finished ! ")  
