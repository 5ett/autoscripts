import pandas as pd
import csv
import html5lib
import requests 
from datetime import datetime
from bs4 import BeautifulSoup as bs

data_src = requests.get('https://worldometers.info/coronavirus').text

parsed_data = bs(data_src, 'html5lib')

potlist = []
potlist2 = []
potlist3 = []
pot_percent = []

date = datetime.utcnow().date


with open('covid-19_total.csv', 'w') as cvd:
	cvdsv = csv.writer(cvd)
	cvdsv.writerow(['DATE', 'TOTAL CASES', 'DEATH', 'RECOVERIES'])
	counters = parsed_data.find('div', class_='content-inner')
	for pot in counters.find_all('div', class_='maincounter-number'):
		potlist.append(pot.text)	
	total, death, recov = potlist
	cvdsv.writerow([ date, total, death, recov])
	
		
with open('covid-19_deatiled.csv', 'w') as cvdd:
	cvddsv = csv.writer(cvdd)
	cvddsv.writerow([" ", " "," ",'ACTIVE CASES', " ", " ", " ", " ", 'CLOSED CASES'])
	cvddsv.writerow(['DATE','TOTAL', 'MILD CASES','%', 'CRITICAL CASES','%','TOTAL', 'RECOVERIES', '%', 'DEATHS', '%'])
	for pot2 in counters.find_all('div', class_='number-table-main'):
		potlist2.append(pot2.text)
		
	for pot3 in counters.find_all('span', class_='number-table'):
		potlist3.append(pot3.text)
		
	total1, total2 = potlist2
	mild, crit, recovv, deathh = potlist3
	cvddsv.writerow([date, total1, mild," ", crit," ", total2, recovv," ", deathh, " "])	
	
	

	

	
		





	

		
#print(potlist)
#print (potlist2)	
#print (potlist3)
	