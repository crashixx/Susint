from utils.plugin.susint_base import *

def socialchecker(socials, working_socials, usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8):
    
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
        if res7.status_code == int(200):
            working_socials.append(social + usr7)
        else:
            pass

        res8 = get(social + usr8)
        if res8.status_code == int(200):
            working_socials.append(social + usr8)
        else:
            pass