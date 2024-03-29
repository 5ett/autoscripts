import requests
import json
from datetime import datetime
from colorama import init
from termcolor import colored

init()
today = datetime.utcnow().date()
time = datetime.utcnow().time()

worldwide = "https://corona-virus-stats.herokuapp.com/api/v1/cases/general-stats"

payload = {}
headers = {}

def recheckk():
	recheck = input(colored("\nCheck another country? (Y/N) ", 'yellow'))
	if recheck == 'Y':
		checker()
	elif recheck == 'N':
		pass
	else:
		print(colored("make sure your reply was either 'Y' or 'N'"))
		recheckk()

def checker():
	country = input(colored("Choose Country: ", 'green'))
	country_data = f"https://covidapi.info/api/v1/country/{country}/latest"
	global_query = input(colored('include global stats?(Y/N) ', 'green'))
	try:
		country_data = requests.get(country_data, headers=headers, data=payload)
		new_country_data = json.loads(country_data.text)['result']
		
		for key, other_value in new_country_data.items():
			date = key
			confirmed = other_value['confirmed']
			country_deaths = other_value['deaths']
			recoveries = other_value['recovered']
	except:
		print(colored('**Make sure you entered an ISO3 country code', 'red'))
		pass
	
	if global_query == 'Y':
		newdata = requests.get(worldwide, headers=headers, data=payload)
		global_data = json.loads(newdata.text)['data']
		total = global_data['total_cases']
		recovery = global_data['recovery_cases']
		deaths = global_data['death_cases']
		recov_perecent = global_data['closed_cases_recovered_percentage']
		death_percent = global_data['closed_cases_death_percentage']
     
		print(f'\n{today} | {time}')
		print(colored("\n\nGlobal Situation", 'white', 'on_green'), end='')
		print(colored(f'\n\tTotal Confirmed Cases: {total}', 'red'))
		print(colored(f'\tRecorded Recoveries: {recovery}({recov_perecent})', 'green'))
		print(colored(f'\tRecorded Deaths: {deaths}({death_percent})\n', 'red'))
	else:
		pass

	if country and country_data:
		print(colored(f"Situation in {country}", 'white', 'on_green'), end='')
		print(colored(f'\n\tTotal Confirmed Cases: {confirmed:,}', 'red'))
		print(colored(f'\tRecorded Recoveries: {recoveries:,}', 'green'))
		print(colored(f'\tRecorded Deaths: {country_deaths:,}', 'red'))
	else:
		checker()
	
	recheckk()

print(colored('**Note\n \tuse ISO3 country codes like...', 'red'))
print(colored('\tITA - Italy\n \tGHA - Ghana\n \tFRA - France\n \tIND - India\n \t...etc', 'red'))

checker()

