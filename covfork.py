import csv
import os
import html5lib
import requests
# from wrkspc import intfy, leap, content
from datetime import datetime
from bs4 import BeautifulSoup as bs

data_src = requests.get('https://worldometers.info/coronavirus').text

# Gh_cases = requests.get('http://www.ghanahealthservice.org/covid19').text

wrk_dir = os.getcwd()

parsed_data = bs(data_src, 'html5lib')
date = datetime.utcnow().date()
time = datetime.utcnow().time()

counters = parsed_data.find('div', class_='content-inner')

int_set = []
pot_percent = []
#increase 
nd_nr = []
leapt = []
total_perc = []


#overview data csv data
if 'covid-19_total.csv' in os.listdir(wrk_dir):
	cvd = open('covid-19_total.csv', 'a')
	cvdsv = csv.writer(cvd)
else:
	cvd = open('covid-19_total.csv', 'w')
	cvdsv = csv.writer(cvd)
	cvdsv.writerow(['DATE', 'TOTAL CASES', 'NEW CASES', 'DEATH', 'NEW DEATHS', 'RECOVERIES', 'NEW RECOV'])
	
	
#detailed data csv file
if 'covid-19_detailed.csv' in os.listdir(wrk_dir):		
	cvdd = open('covid-19_detailed.csv', 'a')
	cvddsv = csv.writer(cvdd)
else:
	cvdd = open('covid-19_detailed.csv', 'w')
	cvddsv = csv.writer(cvdd)
	cvddsv.writerow([" ", " "," ",'ACTIVE CASES', " ", " ", " ", " ", 'CLOSED CASES'])
	cvddsv.writerow(['DATE','TOTAL', 'MILD CASES','%', 'CRITICAL CASES','%','TOTAL', 'RECOVERIES', '%', 'DEATHS', '%'])


leap_fwd = []
leap_pcnt = []
content = []

def intfy( numb, listval):
    hund, thou = numb.split(',')
    res_int = int(hund + thou)
    listval.append(res_int)

def leap(newtotal, listval, desig):
    c = open('covid-19_total.csv')
    reader = csv.DictReader(c)
    for row in reader:
        content.append(row[desig])
    if len(content) > 0:
        oldtotal = content[-1].strip('\n')
        oldtotall = oldtotal.split(' ')
        if len(oldtotall) > 1:
            odl, _ = oldtotall
            hund, thou = odl.split(',')
            odl = hund + thou
            old = int(odl)
        else:
            hund, thou = oldtotal.split(',')
            old_str = hund + thou
            old = int(old_str)

        hund_, thou_ = newtotal.split(',')
        new_str = hund_ + thou_
        new = int(new_str)

        leapfwd = new - old
        leappcnt = ((leapfwd/ old) * 100)
        leappcnt = round(leappcnt, 2)
        listval.append(leapfwd)
        listval.append(leappcnt)
    else:
        listval.append(0)
        listval.append(0)    


potlist = []
for pot in counters.find_all('div', class_='maincounter-number'):
	potlist.append(pot.text.strip())	
total, death, recov = potlist

leap(total, leapt, 'TOTAL CASES')
leap(death, nd_nr, 'DEATH')
leap(recov, nd_nr, 'RECOVERIES')

new_cases, new_caseperc = leapt
nd, nd_perc, nr, nr_perc = nd_nr

intfy(death, total_perc)
intfy(recov, total_perc)

death_int, recov_int = total_perc
nrnd_total = death_int + recov_int
death_per = (death_int/nrnd_total) * 100
death_per = round(death_per, 2)
recov_Per = (recov_int/nrnd_total) * 100
recov_Per = round(recov_Per, 2)


cvdsv.writerow([ 
	f'{date} - {time}', total, f'+{new_cases} ({new_caseperc}%)', f'{death} ({death_per}%)', f'+{nd} ({nd_perc}%)', f'{recov} ({recov_Per}%)', f'+{nr} ({nr_perc}%)'
	])
		

potlist2 = []						
for pot2 in counters.find_all('div', class_='number-table-main'):
	pot2_content = pot2.text.strip()
	intfy(pot2.text, int_set)
	potlist2.append(pot2_content)
		

potlist3 = []				
for pot3 in counters.find_all('span', class_='number-table'):
	pot3_content = pot3.text.strip()
	potlist3.append(pot3_content)
	intfy(pot3.text, int_set)


total1, total2 = potlist2
mild, crit, recovv, deathh = potlist3
int_total1, int_total2, int_mild, int_crit, int_recovv, int_deathh = int_set
	
mild_per = (int_mild/int_total1) * 100
crit_per = (int_crit/int_total1) * 100
	
recovv_per = (int_recovv/int_total2) * 100
deathh_per = (int_deathh/int_total2) * 100
	
cvddsv.writerow([f'{date} - {time}', total1, mild, f'{mild_per}%', crit, f'{crit_per}%', total2, recovv, f'{recovv_per}%', deathh, f'{deathh_per}%'])	
	
	

	
print('done!')
	
		
cvd.close()
cvdd.close()




	

		
#print(potlist)
#print (potlist2)	
#print (potlist3)
	