from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import ceil
from datetime import date


searchword = "alugar ap 1 qt 30 a 50m2 ate 1700 reais no DF"

url = "https://www.dfimoveis.com.br/aluguel/df/todos/apartamento?quartosinicial=1&quartosfinal=1&valorinicial=0&valorfinal=1700&areainicial=30&areafinal=50"

chrmedriv = "C:/Users/VNFSK/Downloads/chromedriver_win32 (1)/chromedriver.exe"

wd = webdriver.Chrome(chrmedriv)
wd.get(url)
wd.maximize_window()
time.sleep(5)


no_of_aps = wd.find_element(By.CSS_SELECTOR, "body > main > main > div.section.container > div.item-center > div.list-container > div.text-imv > div.h-center > h1").text
no_of_aps = int("".join(i for i in no_of_aps.split(" ")[0] if i.isdigit()))

aps_per_page = 30
no_of_pages = ceil(no_of_aps / aps_per_page) + 2



pages = []
for pagenum in range(2, no_of_pages):
    pages0 = url + "&pagina=" + str(pagenum)
    pages.append(pages0)




ap_id = []
link = []
nome_bairro = []
algl = []
condo = []
m2tot = []
m2util = []
qts = []
suite = []
vagas = []
mini_desc = []
res_desc = []


##for loop over pages
for page in pages:


    no_of_ads_in_page = len(wd.find_elements(By.CLASS_NAME, 'new-card'))
    print("ads per page: " + str(no_of_ads_in_page))


    ##for loop over ads in page
    for ad_num in range(1, no_of_ads_in_page + 1):


##        try:
##            ap_id0 = wd.find_element(By.CSS_SELECTOR, "").get_attribute("data-id")
##            ap_id.append(ap_id0)
##        except:
        ap_id0 = ""
        ap_id.append(ap_id0)

        
        try:
            link0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ")").get_attribute("href")
            link.append(link0)
        except:
            link0 = ""
            link.append(link0)


        try:
            nome_bairro0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-header > div > h2").text
            nome_bairro.append(nome_bairro0)
        except:
            nome_bairro0 = ""
            nome_bairro.append(nome_bairro0)


        try:
            algl0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-price-detail > div.new-price > h4:nth-child(1) > span").text
            algl.append(algl0)
        except:
            algl0 = ""
            algl.append(algl0)


##        try:
##            condo0 = wd.find_element(By.CSS_SELECTOR, "" + str(ad_num) + "").text
##            condo.append(condo0)
##        except:
        condo0 = ""
        condo.append(condo0)


##        try:
##            m2tot0 = wd.find_element(By.CSS_SELECTOR, "" + str(ad_num) + "").text
##            m2tot.append(m2tot0)
##        except:
        m2tot0 = ""
        m2tot.append(m2tot0)


        try:
            m2util0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-price-detail > ul > li.m-area > span").text
            m2util.append(m2util0)
        except:
            m2util0 = ""
            m2util.append(m2util0)


        try:
            qts0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-price-detail > ul > li:nth-child(2) > span").text
            qts.append(qts0)
        except:
            qts0 = ""
            qts.append(qts0)


        try:
            suite0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-price-detail > ul > li:nth-child(3) > span").text
            suite.append(suite0)
        except:
            suite0 = ""
            suite.append(suite0)


        try:
            vagas0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-price-detail > ul > li:nth-child(4) > span").text
            vagas.append(vagas0)
        except:
            vagas0 = ""
            vagas.append(vagas0)


        try:
            mini_desc0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > h3").text
            mini_desc.append(mini_desc0)
        except:
            mini_desc0 = ""
            mini_desc.append(mini_desc0)


        try:
            res_desc0 = wd.find_element(By.CSS_SELECTOR, "#resultadoDaBuscaDeImoveis > a:nth-child(" + str(ad_num) + ") > div.new-info > div.new-text.phrase").text
            res_desc.append(res_desc0)
        except:
            res_desc0 = ""
            res_desc.append(res_desc0)



    wd.quit()
    wd = webdriver.Chrome(chrmedriv)
    wd.get(page)
    wd.maximize_window()
    time.sleep(5)



ap_data = pd.DataFrame({
    "ap_id": ap_id,
    "link" : link,
    "nome_bairro" : nome_bairro,
    "algl" : algl,
    "condo" : condo,
    "m2tot" : m2tot,
    "m2util" : m2util,
    "qts" : qts,
    "suite" : suite,
    "vagas" : vagas,
    "mini_desc" : mini_desc,
    "res_desc" : res_desc
    })


ap_data.to_csv("dfimoveis ap data - "  + str(no_of_aps) + " results searching " + searchword + " - " + str(date.today()) +  ".csv", index = False)



