import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs
from safe_get import fetch_html

SITE_URL = "https://bloknot-volgograd.ru"

async def download_news_urls(session):
    url = "https://bloknot-volgograd.ru/news/policy/"
    html = await fetch_html(url, session)
    news_urls = parse_news(html)
    return news_urls


# выдает статьи
def parse_news(news_html):
    html = bs(news_html, 'html.parser')
    urls = html.find_all(class_='linksys')
    urls = [SITE_URL + url['href'] for url in urls]
    return urls


# Возвращшает распаршенную статью
async def parse_article(url, session):
    html = await fetch_html(url, session)
    html = bs(html, 'html.parser')
    title = html.find('article').find('h1').text
    date = html.find('span', class_='news-date-time').text
    link = url
    text = html.find(id='news-text').text


    article = {
        'title': title,
        'date': date,
        'link': link,
        'text': text,
    }

    return article
