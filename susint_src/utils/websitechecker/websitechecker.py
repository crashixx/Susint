from utils.plugin.susint_base import *

def websitechecker(start_url, domains, working_domains, users):
    for user in users:
        for s_url in start_url:
            for dm in domains:
                request= s_url + user + dm
                try:
                    get(request)
                    working_domains.append(request)
                except:
                    pass
