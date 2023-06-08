import sqlite3

import requests as req
import bs4
from requests import TooManyRedirects

url = 'https://onlinenursingessays.com/blog/'

base = sqlite3.connect('parser.db')
cursor = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS onlinenursingessays(title text, url text, article text)')

error_links = []

for i in range(2486, 4685):
    print(i)
    page = req.get(url + f"page/{i}/")
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    allLinks = soup.findAll('a', rel="bookmark")
    for elem in allLinks:
        title = elem.get_text()
        link = elem["href"]
        try:
            blog = req.get(link)
            blog_soup = bs4.BeautifulSoup(blog.text, "html.parser")
            article = str(blog_soup.find('article'))
            rubbish = list(map(str, blog_soup.findAll('div', class_="wp-block-kadence-column")))
            for bad_code in rubbish:
                article = article.replace(bad_code, "")
            cursor.execute('INSERT INTO onlinenursingessays VALUES (?, ?, ?)', (title, link, article))
        except TooManyRedirects:
            print(link)
            error_links.append(link)
    base.commit()
