from utils.plugin.susint_base import *

def socialchecker(socials, users, working_socials ):
    
    #instgram dedicated checker
    for user in users:
        res = get(url = f"https://www.instagram.com/{user}")
        soup = BeautifulSoup(res.text, "html.parser")
        if soup(text=lambda t: user in t.text) != []:
            working_socials.append(f'https://www.instagram.com/{user}')


    for social in socials:
        for user in users:
            res = get(social + user)
            if res.status_code == 200:
                working_socials.append(social + user)
            elif res.status_code == 404:
                pass
