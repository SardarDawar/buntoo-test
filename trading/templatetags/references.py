from django import template
import requests 
from bs4 import BeautifulSoup
import re
register = template.Library()
import json
@register.filter('references')
def reference_finder(value):
  
    print(value)
    
    headers_Get = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    q=value

    request = requests.Session()
    q_search = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q_search + '&ie=utf-8&oe=utf-8'
    page = request.get(url, headers=headers_Get)

    soup = BeautifulSoup(page.text, "html.parser")
    response = soup.find_all('div',class_='rc')
    first_three = []
    matching = []
    for i in response:
        first_three.append(i.find('a').attrs['href'])
        

    # for i in first_three:
    #     pages =request.get(i)
    #     result = BeautifulSoup(pages.text, "html.parser")
    #     matching.append(re.findall(q,result.text))

    return first_three