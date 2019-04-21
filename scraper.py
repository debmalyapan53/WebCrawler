import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.values.com/inspirational-quotes' #page
page = requests.get(url)  #open page
soup = BeautifulSoup(page.content,'html5lib')    #soup object containing the html of the page
#print(soup.prettify())  #representation of the parse tree

quotes=[]
table = soup.find('div', attrs = {'id':'portfolio'}) 
  
for row in table.findAll('div', attrs = {'class':'portfolio-image'}): 
    quote = {} 
    #quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    #quote['lines'] = row.h6.text 
    text = row.img['alt'].encode("utf-8") 
    quote['quote'] = text.split('.',1)[0]
    quotes.append(quote) 
  
filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['url','img','quote']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote)