from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import ceil
from datetime import date
import csv


chrmedriv = "C:/Users/VNFSK/Downloads/chromedriver_win32 (1)/chromedriver.exe"



links = []
with open("C:/Users/VNFSK/Downloads/dfimoveis ap data - 699 results searching alugar ap 1 qt 30 a 50m2 ate 1700 reais no DF - 2023-02-12.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    link0 = row[1]
    links.append(link0)

links = links[1:]



condo = []
desc = []
detalhes = []

for link in links:

    wd = webdriver.Chrome(chrmedriv)
    wd.get(link)
    wd.maximize_window()
    time.sleep(3)
    
    
    try:
        condo0 = wd.find_element(By.CSS_SELECTOR, "body > main > section > div > div.row.row-grid.align-items-center > div > div > div.r-computador-dados > div.row.justify-content-between.flex-row.flex-nowrap.mt-1.mb-2 > div:nth-child(1) > h6 > small").text
        condo.append(condo0)
    except:
        condo0 = ""
        condo.append(condo0)
        

    try:
        desc0 = wd.find_element(By.CSS_SELECTOR, "body > main > section > div > div.row.row-grid.align-items-center > div > div > div:nth-child(5) > p").text
        desc.append(desc0)
    except:
        desc0 = ""
        desc.append(desc0)
        

    try:
        detalhes0 = wd.find_element(By.CSS_SELECTOR, "body > main > section > div > div.row.row-grid.align-items-center > div > div > div.col-md-12.bg-white.shadow.mt-2.pb-2").text
        detalhes.append(detalhes0)
    except:
        detalhes0 = ""
        detalhes.append(detalhes0)


    wd.quit()



ap_data = pd.DataFrame({
    "link" : links,
    "condo" : condo,
    "detalhes" : detalhes,
    "desc" : desc
    })


ap_data.to_csv("dfimoveis additional ap data - " + str(date.today()) +  ".csv", index = False)
    



    
