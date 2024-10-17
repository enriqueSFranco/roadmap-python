import requests
from bs4 import BeautifulSoup

URL='https://www.nin-nin-game.com/es/'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
PRODUCT_TO_FIND='saint-seiya-myth-cloth'

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# buscar el formulario que contenga el input de busqueda
form_element = soup.find(id='searchbox')
input_search = form_element.find(id='search_query_top')

# dar click al input e introducir una busqueda
