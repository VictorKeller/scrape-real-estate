from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import ceil
from datetime import date


searchword = "alugar ap 1 qt 30 a 50m2 ate 1700 reais no DF"

url = "https://www.wimoveis.com.br/apartamentos-aluguel-distrito-federal-ate-1-quarto-30-50-m2-util-menos-1700-reales.html"

chrmedriv = "C:/Users/VNFSK/Downloads/chromedriver_win32 (1)/chromedriver.exe"

wd = webdriver.Chrome(chrmedriv)
wd.get(url)
wd.maximize_window()
time.sleep(3)


no_of_aps = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.sc-5z85om-0.hjpEnc > div.sc-5z85om-2.czixvV > h1").text
no_of_aps = int("".join(i for i in no_of_aps.split(" ")[0] if i.isdigit()))


no_of_pages = ceil(no_of_aps / 20)



pages = []
for pagenum in range(2, no_of_pages):
    pages0 = url[0:-5] + "-pagina-" + str(pagenum) + ".html"
    pages.append(pages0)

##pages = [url] + pages


ap_id = []
link = []
nome = []
bairro = []
algl = []
condo = []
m2tot = []
m2util = []
qts = []
banhs = []
vagas = []
mini_desc = []
desc = []


##for loop over pages
for page in pages:


    no_of_ads_in_page = len(wd.find_elements(By.CLASS_NAME, 'sc-1tt2vbg-3'))


    ##for loop over ads in page
    for ad_num in range(1, no_of_ads_in_page + 1):


        try:
            ap_id0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div").get_attribute("data-id")
            ap_id.append(ap_id0)
        except:
            ap_id0 = ""
            ap_id.append(ap_id0)


        try:
            link0 = "https://www.wimoveis.com.br" + wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div").get_attribute("data-to-posting")
            link.append(link0)
        except:
            link0 = ""
            link.append(link0)


        try:
            nome0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div.sc-i1odl-0.cYmZqs > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.cypYcv > div.sc-ge2uzh-1.dhzcWt > div.sc-ge2uzh-0.bzGYzE").text
            nome.append(nome0)
        except:
            nome0 = ""
            nome.append(nome0)


        try:
            bairro0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div.sc-i1odl-0.cYmZqs > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.cypYcv > div.sc-ge2uzh-1.dhzcWt > div.sc-ge2uzh-2.hWApJB").text
            bairro.append(bairro0)
        except:
            bairro0 = ""
            bairro.append(bairro0)


        try:
            algl0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.cypYcv > div.sc-i1odl-8.hmHSY > div.sc-12dh9kl-0.cysiyu > div.sc-12dh9kl-3.gGCVnu > div").text
            algl.append(algl0)
        except:
            algl0 = ""
            algl.append(algl0)


        try:
            condo0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.cypYcv > div.sc-i1odl-8.hmHSY > div.sc-12dh9kl-0.cysiyu > div.sc-12dh9kl-2.bTjrHB").text
            condo.append(condo0)
        except:
            condo0 = ""
            condo.append(condo0)


        try:
            m2tot0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.bkbRHX > div > span:nth-child(1) > span").text
            m2tot.append(m2tot0)
        except:
            m2tot0 = ""
            m2tot.append(m2tot0)


        try:
            m2util0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.bkbRHX > div > span:nth-child(2) > span").text
            m2util.append(m2util0)
        except:
            m2util0 = ""
            m2util.append(m2util0)


        try:
            qts0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.bkbRHX > div > span:nth-child(3) > span").text
            qts.append(qts0)
        except:
            qts0 = ""
            qts.append(qts0)


        try:
            banhs0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.bkbRHX > div > span:nth-child(4) > span").text
            banhs.append(banhs0)
        except:
            banhs0 = ""
            banhs.append(banhs0)


        try:
            vagas0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-5.bkbRHX > div > span:nth-child(5) > span").text
            vagas.append(vagas0)
        except:
            vagas0 = ""
            vagas.append(vagas0)


        try:
            mini_desc0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > h2 > a").text
            mini_desc.append(mini_desc0)
        except:
            mini_desc0 = ""
            mini_desc.append(mini_desc0)


        try:
            desc0 = wd.find_element(By.CSS_SELECTOR, "#root > div.sc-ps0squ-0.hiZnfm > div > div > div.sc-185xmk8-1.iNSUmi > div.sc-185xmk8-2.bqddpd > div.postings-container > div:nth-child(" + str(ad_num) + ") > div > div > div.sc-i1odl-2.gIHCpf > div.sc-i1odl-3.VSxgr > div:nth-child(1) > div.sc-i1odl-12.kiOjEU").text
            desc.append(desc0)
        except:
            desc0 = ""
            desc.append(desc0)



    wd.quit()
    wd = webdriver.Chrome(chrmedriv)
    wd.get(page)
    time.sleep(3)



ap_data = pd.DataFrame({
    "ap_id": ap_id,
    "link" : link,
    "nome" : nome,
    "bairro" : bairro,
    "algl" : algl,
    "condo" : condo,
    "m2tot" : m2tot,
    "m2util" : m2util,
    "qts" : qts,
    "banhs" : banhs,
    "vagas" : vagas,
    "mini_desc" : mini_desc,
    "desc" : desc
    })


ap_data.to_csv("wimoveis ap data - "  + str(no_of_aps) + " results searching " + searchword + " - " + str(date.today()) +  ".csv", index = False)



