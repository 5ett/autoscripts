import pandas as pd
import csv
import os
import html5lib
import requests 
from datetime import datetime
from bs4 import BeautifulSoup as bs

data_src = requests.get('https://worldometers.info/coronavirus').text

#Gh_cases = requests.get('http://www.ghanahealthservice.org/covid19').text

wrk_dir = os.getcwd()

parsed_data = bs(data_src, 'html5lib')
date = datetime.utcnow()
time = datetime.utcnow().time

counters = parsed_data.find('div', class_='content-inner')
int_set = []
pot_percent = []

#overview data csv data
if 'covid-19_total.csv' in os.listdir(wrk_dir):
	cvd = open('covid-19_total.csv', 'a')
	cvdsv = csv.writer(cvd)
else:
	cvd = open('covid-19_total.csv', 'w')
	cvdsv = csv.writer(cvd)
	cvdsv.writerow(['DATE', 'TOTAL CASES', 'DEATH', 'RECOVERIES'])
	
	
#detailed data csv file
if 'covid-19_detailed.csv' in os.listdir(wrk_dir):		
	cvdd = open('covid-19_detailed.csv', 'a')
	cvddsv = csv.writer(cvdd)
else:
	cvdd = open('covid-19_detailed.csv', 'w')
	cvddsv = csv.writer(cvdd)
	cvddsv.writerow([" ", " "," ",'ACTIVE CASES', " ", " ", " ", " ", 'CLOSED CASES'])
	cvddsv.writerow(['DATE','TOTAL', 'MILD CASES','%', 'CRITICAL CASES','%','TOTAL', 'RECOVERIES', '%', 'DEATHS', '%'])

		
potlist = []
for pot in counters.find_all('div', class_='maincounter-number'):
	potlist.append(pot.text)	
total, death, recov = potlist
cvdsv.writerow([ f'{date} - {time}', total, death, recov])
		

potlist2 = []						
for pot2 in counters.find_all('div', class_='number-table-main'):
	hund, thou = pot2.text.split(',')
	resulting_int = int(hund + thou)
	int_set.append(resulting_int)
	potlist2.append(pot2.text)
		

potlist3 = []				
for pot3 in counters.find_all('span', class_='number-table'):
	potlist3.append(pot3.text)
	hund_, thou_ = pot3.text.split(',')
	res_int = int(hund_ + thou_)
	int_set.append(res_int)
	
	
		
total1, total2 = potlist2
mild, crit, recovv, deathh = potlist3
int_total1, int_total2, int_mild, int_crit, int_recovv, int_deathh = int_set
	
mild_per = (int_mild/int_total1) * 100
crit_per = (int_crit/int_total1) * 100
	
recovv_per = (int_recovv/int_total2) * 100
deathh_per = (int_deathh/int_total2) * 100
	
cvddsv.writerow([f'{date} - {time}', total1, mild, f'{mild_per}%', crit, f'{crit_per}%', total2, recovv, f'{recovv_per}%', deathh, f'{deathh_per}%'])	
	
	

	

	
		
cvd.close()
cvdd.close()




	

		
#print(potlist)
#print (potlist2)	
#print (potlist3)
	