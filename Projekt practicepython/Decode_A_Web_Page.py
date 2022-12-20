# CEL: Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# on the onet homepage.

from bs4 import BeautifulSoup
import requests

header_list = []
url = "https://www.onet.pl"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

for heading in soup.find_all('h3'):
    header_list.append(heading.text)

print(header_list)
