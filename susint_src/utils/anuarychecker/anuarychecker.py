from utils.plugin.susint_base import *

def anuarychecker(driver, adress, nums, usr):

    driver.get(f"https://www.annuaire-inverse.mobi/pro/search?q={usr}")

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