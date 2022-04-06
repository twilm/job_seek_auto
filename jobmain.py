from bs4 import BeautifulSoup
import requests

###This is the code to pull HTML from Jora's default search sorted by Date 
html_text = requests.get('https://au.jora.com/jobs-in-Maryborough-QLD?sp=facet&l=Maryborough+QLD&st=date').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find('div', class_ = "jobresults").find_all('article')
#job_title = job.text.replace(' ', ' ')
 
class mboro_jobsearch:
	def print():
		for job in jobs:
			location = job.find('span', class_= 'job-location').text.strip()
			if 'Maryborough' in location:
				company_name = job.find('span', class_ = 'job-company').text.strip()
				job_title = job.find('h3', class_='job-title').text.strip()
				
				print(f'''		
				Company Name: {company_name}
				Location: {location}
				Job Title: {job_title}
				''')


class hbay_jobsearch:
	def print():
		for job in jobs:
			location = job.find('span', class_= 'job-location').text.strip()
			if 'Hervey' in location:
				company_name = job.find('span', class_ = 'job-company').text.strip()
				job_title = job.find('h3', class_='job-title').text.strip()
				
				print(f'''		
				Company Name: {company_name}
				Location: {location}
				Job Title: {job_title}
				''')


m = mboro_jobsearch
h = hbay_jobsearch




print("H for Hervey Bay, M for Maryborough    ")
searchLocal = str(input())
if searchLocal == 'H' or 'h':
	h.print()
elif searchLocal == 'M' or 'm':
	m.print()
else:
	print('poopoopeepee')
  


