from utils.plugin.susint_base import *

def mail_checker(usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8, api_keys, valid_mails):
    
    mails = []

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
    mails.append(f"{usr7}{host1}")
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
        response = get("https://isitarealemail.com/api/email/validate",params = {'email': email}, headers = {'Authorization': f"Bearer {api_keys['mail_api']}" })

        status = response.json()['status']
        if status == "valid":
            valid_mails.append(email)
        elif status == "invalid":
            pass