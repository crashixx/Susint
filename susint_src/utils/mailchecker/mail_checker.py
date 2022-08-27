from utils.plugin.susint_base import *

def mail_checker(users, api_keys, valid_mails):
    
    mails = []
    host = ["@yandex.ru","@hotmail.com","@outlook.com","@yahoo.com","@gmail.com","@icloud.com","@aol.com","@msn.com","@live.com"]

    for user in users:
        for h in range(len(host)):
            mails.append(f"{user}{host[h]}")


    #email checker
    for email in mails:
        response = get("https://isitarealemail.com/api/email/validate",params = {'email': email}, headers = {'Authorization': f"Bearer {api_keys['mail_api']}" })

        status = response.json()['status']
        if status == "valid":
            valid_mails.append(email)
        else:
            pass
