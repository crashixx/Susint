from utils.plugin.susint_base import *

def deathrecorder(firstname, name, profile_found):
    response = get(f"https://www.libramemoria.com/avis?nom={name}&prenom={firstname}")    
    content = response.content
    parser = "html.parser"
    site = BeautifulSoup(content, parser)

    names  = site.find_all('div',{'class':'cellule nom alone'})
    ages   = site.find_all('div',{'class':'cellule age hideXs_tablecell alone'})
    villes = site.find_all('div',{'class':'cellule ville liste_virgule alone'})

    for x in range(len(names)):
        try:
            _name = names[x].text.split('(')[0].replace('\r','').replace('\n','').replace('\t','').strip()
            age = ages[x].text.replace("ans","Years old").strip()
            ville = villes[x].text.replace('\r','').replace('\n','').replace('\t','').replace('(',' (').strip()
            all = f"Name: {_name}\nAge: {age}\nVille: {ville}"
            profile_found.append(all)
        except:
            pass
        
