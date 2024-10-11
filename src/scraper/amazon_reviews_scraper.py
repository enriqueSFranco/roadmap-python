import requests
import json
from bs4 import BeautifulSoup


URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

job_elements = results.find_all('div', class_='card-content')

# for job_element in job_elements:
#   title = job_element.find('h2', class_='title')
#   subtitle = job_element.find('h3', class_='subtitle')
#   location = job_element.find('p', class_='location')

#   title.text.strip()
#   subtitle.text.strip()
#   location.text.strip()  
#   print(f'{title, subtitle, location}', end='\n'*2)


python_jobs = results.find_all(
  'h2',
  string=lambda text: 'python' in text.lower()
)

# for python_job in python_jobs:
#   print(python_job)
#   title = python_job.find('h2', class_='title')
#   company = python_job.find('h3', class_='subtitle')
#   location = python_job.find('p', class_='location')

#   title_text = title.text.strip()  
#   company_text = company.text.strip()
#   location_text = location.text.strip()
#   print(f'Vacante: {title}, \Empresa: {company}, \nUbicacion: {location}', end='\n'*2)

python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

my_jobs = []
for python_job_element in python_job_elements:
  title_element = python_job_element.find('h2', class_='title')
  company_element = python_job_element.find('h3', class_='subtitle')
  location_element = python_job_element.find('p', class_='location')
  link_elements = python_job_element.find_all('a')[1] # Ejercicio: Obtener solo el segundo link

  title = title_element.text.strip()
  company = company_element.text.strip()
  location = location_element.text.strip()
  link = link_elements['href']

  job_info = {
    "title": title,
    "company": company, 
    "location": location,
    "links": link
  }

  # for link_element in link_elements:
  #   url = link_element['href']
  #   job_info['links'].append(url)

  my_jobs.append(job_info)

print(json.dumps(my_jobs, indent=4, ensure_ascii=False))