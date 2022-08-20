
from requests import get 
from selenium import webdriver
from os import environ as env, path as _path, system as sys, getcwd
from colorama import Fore
from time import sleep
from pystyle import Anime, Center, Colors, Colorate, System
from pypresence import Presence
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes

#=========================== rich presence ===========================

try:
    rpc = Presence("713734159574630420")
    rpc.connect()
    rpc.update(state="by crashixx",details=f"OSINT tool",large_image="logo_resize_")
except:
    pass

#=========================== silly defs ===========================

def clear():
    sys("cls")

#=========================== silly vars ===========================
#colors 
y = Fore.MAGENTA
b = Fore.LIGHTBLACK_EX
w = Fore.LIGHTWHITE_EX

program_file = env["ProgramW6432"]
program_file_2 = env["ProgramFiles"]
program_file_x86 = env["ProgramFiles(x86)"]


#mail api key go to (https://isitarealemail.com/) to create one for free
api_key = "ENTER YOUR API KEY HERE"

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

#=========================== firefox checker ===========================

if _path.exists(f"{program_file}\\Mozilla Firefox\\firefox.exe") == True:
    firefox_path = f"{program_file}\\Mozilla Firefox\\firefox.exe" 
elif _path.exists(f"{program_file_x86}\\Mozilla Firefox\\firefox.exe") == True:
    firefox_path = f"{program_file_x86}\\Mozilla Firefox\\firefox.exe"
elif _path.exists(f"{program_file_2}\\Mozilla Firefox\\firefox.exe") == True:
    firefox_path = f"{program_file_2}\\Mozilla Firefox\\firefox.exe"
else:
    clear()
    print(banner)
    firefox_path = input(f"{y}[{w}#{y}]{w}Le navigateur firefox n'est pas detecté !...\n{y}[{w}#{y}]{w}Est-il installé?\n=~=~=\n{y}[{w}#{y}]{w}Si oui entrez le chemin d'acces ici:\n>>>")
    exit()

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
7
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
    usr8= f"-_{username}_-"
#=========================== email reserch per fisrtname and secondname ===========================

mails = []
valid_mails = []

#hostlist
host1 = "@gmail.com"
host2 = "@orange.fr"


# mail list host 1
mails.append(f"{usr1}{host1}")
mails.append(f"{usr2}{host1}")
mails.append(f"{usr3}{host1}")
mails.append(f"{usr4}{host1}")
mails.append(f"{usr5}{host1}")
mails.append(f"{usr6}{host1}")
mails.append(f"{usr8}{host1}")
mails.append(f"{usr8}{host1}")

#mail list host 2
mails.append(f"{usr1}{host2}")
mails.append(f"{usr2}{host2}")
mails.append(f"{usr3}{host2}")
mails.append(f"{usr4}{host2}")
mails.append(f"{usr5}{host2}")
mails.append(f"{usr6}{host2}")
mails.append(f"{usr7}{host2}")
mails.append(f"{usr8}{host2}")

#email checker
for email in mails:
    response = get("https://isitarealemail.com/api/email/validate",params = {'email': email}, headers = {'Authorization': f"Bearer {api_key}" })

    status = response.json()['status']
    if status == "valid":
        valid_mails.append(email)
    elif status == "invalid":
        pass

#=========================== adress & telf scraper ===========================

adress = []
nums = []
if choice == str("1"):
    driver.get(f"https://www.annuaire-inverse.mobi/pro/search?q={firstname}+{name}")
elif choice == str("2"):
    driver.get(f"https://www.annuaire-inverse.mobi/pro/search?q={username}")
sleep(3)

#adress scraper
e=driver.find_elements_by_class_name("info")
for x in e:
    adress.append(x.text)

#num scraper
html = driver.page_source
with open(f"page.html","w",encoding="utf-8-sig") as f:
    f.write(str(html))
    f.close()

#read page.html
with open('page.html', "r") as tf:
    datafile = tf.readlines()
    for line in datafile:
        if '"colBtn"' in line:
            characters = r"""<aclass="colBtnhref=>spanApelersanab:%&;/ """
            num = ''.join( x for x in line if x not in characters)
            nums.append(num)

tf.close()
driver.close()


#=========================== social scraper ===========================

socials = ["https://instagram.com/", "https://www.facebook.com/", "https://www.twitch.tv/", "https://twitter.com/","https://pr0gramm.com/user/", "https://www.npmjs.com/~", 
"https://note.com/", "http://www.authorstream.com/", "https://youpic.com/photographer/", "https://www.virustotal.com/ui/users/", "https://vimeo.com/", "https://tryhackme.com/p/", 
"https://tenor.com/users/", "https://open.spotify.com/user/", "https://sourceforge.net/u/", "https://soundcloud.com/", "https://www.smule.com/", "https://scratch.mit.edu/users/", 
"https://replit.com/@","https://raidforums.com/User-", "https://pypi.org/user/", "https://www.pinterest.com/", "https://onlyfans.com/", "https://imgur.com/user/", 
"https://forum.hackthebox.eu/profile/", "https://www.github.com/"]

working_socials = []


for social in socials:

    res1 = get(social + usr1)
    if res1.status_code == int(200):
        working_socials.append(social + usr1)
    else:
        pass

    res2 = get(social + usr2)
    if res2.status_code == int(200):
        working_socials.append(social + usr2)
    else:
        pass

    res3 = get(social + usr3)
    if res3.status_code == int(200):
        working_socials.append(social + usr3)
    else:
        pass

    res4 = get(social + usr4)
    if res4.status_code == int(200):
        working_socials.append(social + usr4)
    else:
        pass

    res5 = get(social + usr5)
    if res5.status_code == int(200):
        working_socials.append(social + usr5)
    else:
        pass

    res6 = get(social + usr6)
    if res6.status_code == int(200):
        working_socials.append(social + usr6)
    else:
        pass

    res7 = get(social + usr7)
    if res6.status_code == int(200):
        working_socials.append(social + usr7)
    else:
        pass

    res8 = get(social + usr8)
    if res6.status_code == int(200):
        working_socials.append(social + usr8)
    else:
        pass


#=========================== website checker ===========================

start_url = ["http://", "https://"]
domains = [".fr", ".es", ".ma", ".uk", ".xyz", ".ga", ".ru", ".com", ".online",
".live", ".store", ".tech", ".site", ".website"]

working_domains = []

for s_url in start_url:
    for dm in domains:
        
        req1= s_url + usr1 + dm
        try:
            res1 = get(req1)
            working_domains.append(req1)
        except:
            pass
        
        req2= s_url + usr2 + dm
        try:
            res2 = get(req2)
            working_domains.append(req2)
        except:
            pass
        
        req3= s_url + usr3 + dm
        try:
            res3 = get(req3)
            working_domains.append(req3)
        except:
            pass
        
        req4= s_url + usr4 + dm
        try:
            res4 = get(req4)
            working_domains.append(req4)
        except:
            pass

        req5= s_url + usr5 + dm
        try:
            res5 = get(req5)
            working_domains.append(req5)
        except:
            pass
        
        req6= s_url + usr6 + dm
        try:
            res6 = get(req6)
            working_domains.append(req6)
        except:
            pass

        req7= s_url + usr7 + dm
        try:
            res7 = get(req7)
            working_domains.append(req7)
        except:
            pass 
        
        req8= s_url + usr8 + dm
        try:
            res8 = get(req8)
            working_domains.append(req8)
        except:
            pass 
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
