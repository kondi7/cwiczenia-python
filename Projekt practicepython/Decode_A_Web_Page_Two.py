from bs4 import BeautifulSoup
import requests

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

for article_text in soup.find_all('p', class_="paywall"):
    print(article_text.text)
