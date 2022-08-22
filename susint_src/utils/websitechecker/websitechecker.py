from utils.plugin.susint_base import *

def websitechecker(start_url, domains, working_domains, usr1, usr2, usr3, usr4, usr5, usr6, usr7, usr8):
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
                res8 = get(s_url + usr8 + dm)
                working_domains.append(req8)
            except:
                pass 