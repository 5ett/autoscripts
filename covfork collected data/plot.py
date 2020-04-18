from matplotlib import pyplot as plt
import csv

recov_content = []
pass_content = []
date_data = []

with open('covid-19_total.csv', encoding='utf8') as cvd19:
    reader = csv.DictReader(cvd19)
    for row in reader:
        date = row['DATE'].split(' ')
        date_data.append(date)
        recovs = row['RECOVERIES'].split(' ')
        recov_content.append(recovs)
        passing = row['DEATH'].split(' ')
        pass_content.append(passing)


val_y = []
la_date = []
for date in date_data:
    D, *_ = date
    la_date.append(D)
for date in la_date:
    *_, mm, dd = date.split('-')
    val_y.append(f'{dd}/{mm}')
    # print(val_y)
    # break

val_x = []
for value in recov_content:
    real_number, _ = value
    val_x.append(int(real_number.replace(',', '')))

plt.plot(val_y, val_x)

val_x2 = []
for value in pass_content:
    real_number, _ = value
    val_x2.append(int(real_number.replace(',', '')))

plt.plot(val_y, val_x2)
plt.title('COVID-19 RECOVERY/DEATHS (march 20 - apr 18)')
plt.legend(['Recoveries', 'Deaths'])
plt.show()
