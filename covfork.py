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
# increase
new_death_recov = []
leapt = []
total_perc = []


# overview data csv data
if 'covid-19_total.csv' in os.listdir(wrk_dir):
    cvd = open('covid-19_total.csv', 'a')
    cvdsv = csv.writer(cvd)
else:
    cvd = open('covid-19_total.csv', 'w')
    cvdsv = csv.writer(cvd)
    cvdsv.writerow(['DATE', 'TOTAL CASES', 'NEW CASES', 'DEATH',
                    'NEW DEATHS', 'RECOVERIES', 'NEW RECOV'])


# detailed data csv file
if 'covid-19_detailed.csv' in os.listdir(wrk_dir):
    cvdd = open('covid-19_detailed.csv', 'a')
    cvddsv = csv.writer(cvdd)
else:
    cvdd = open('covid-19_detailed.csv', 'w')
    cvddsv = csv.writer(cvdd)
    cvddsv.writerow([" ", " ", " ", 'ACTIVE CASES',
                     " ", " ", " ", " ", 'CLOSED CASES'])
    cvddsv.writerow(['DATE', 'TOTAL', 'MILD CASES', '%', 'CRITICAL CASES',
                     '%', 'TOTAL', 'RECOVERIES', '%', 'DEATHS', '%'])


csv_content = []  # list of retrieved string numbers for 'intification'

# convert retrieved string to an integer


def intfy(number, listval):
    print(number)
    number = int(number.replace(',' , ''))
    listval.append(number)
    

# list value = the list to append calculated increases
# desig = the Column heading to retrieve from csv


def leap(newtotal, listval, desig):
    c = open('covid-19_total.csv')
    reader = csv.DictReader(c)
    for row in reader:
        csv_content.append(row[desig])
    if len(csv_content) > 0:
        oldtotal = csv_content[-1].strip('\n')
        oldtotal_1 = oldtotal.split(' ')
        if len(oldtotal_1) > 1:
            odl, _ = oldtotal_1
            old = int(odl.replace(',' , ''))
            print(old)
        else:
            old = int(oldtotal.replace(',', ''))
            
        new = int(newtotal.replace(',', ''))            
        leap_fwd = new - old
        leap_percent = ((leap_fwd / old) * 100)
        leap_percent = round(leap_percent, 2)
        listval.append(leap_fwd)
        listval.append(leap_percent)
    else:
        listval.append(0)
        listval.append(0)


potlist = []
for pot in counters.find_all('div', class_='maincounter-number'):
    potlist.append(pot.text.strip())
total, death, recov = potlist

leap(total, leapt, 'TOTAL CASES')
leap(death, new_death_recov, 'DEATH')
leap(recov, new_death_recov, 'RECOVERIES')

new_cases, new_cases_pcnt = leapt
new_deaths, new_deaths_percent, new_recoveries, new_recoveries_pcnt = new_death_recov

intfy(death, total_perc)
intfy(recov, total_perc)

death_int, recovery_int = total_perc
total_death_recovery = death_int + recovery_int
death_percent = (death_int / total_death_recovery) * 100
death_percent = round(death_percent, 2)
recovery_percent = (recovery_int / total_death_recovery) * 100
recovery_percent = round(recovery_percent, 2)


cvdsv.writerow([
    f'{date} - {time}', total, f'+ {new_cases} ({new_cases_pcnt}%)', f'{death} ({death_percent}%)', f'+ {new_deaths} ({new_deaths_percent}%)', f'{recov} ({recovery_percent}%)', f'+ {new_recoveries} ({new_recoveries_pcnt}%)'
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
mild, critical, recovv, deathh = potlist3
int_total1, int_total2, int_mild, int_critical, int_recovv, int_deathh = int_set

mild_percent = (int_mild / int_total1) * 100
critical_percent = (int_critical / int_total1) * 100

recovery_percent_2 = (int_recovv / int_total2) * 100
death_percent_2 = (int_deathh / int_total2) * 100

cvddsv.writerow([f'{date} - {time}', total1, mild, f'{mild_percent}%', critical,
    f'{critical_percent}%', total2, recovv, f'{recovery_percent_2}%', deathh, f'{death_percent_2}%'])


print('done!')


cvd.close()
cvdd.close()


print(potlist)
print (potlist2)
print (potlist3)
