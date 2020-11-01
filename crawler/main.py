import asyncio
import os
import json
from crawler import *
import uuid


async def main():
    print('Начинаем выбирать новости')

    async with aiohttp.ClientSession() as session:
        urls = await download_news_urls(session)
        print('Новости выбраны, начинаем обработку статей')

        jobs = [parse_article(url, session) for url in urls]

        articles = await asyncio.gather(*jobs)
        for article in articles:
            article['id'] = str(uuid.uuid1())

    print('Получено статей с главной страницы', len(articles))
    
    if not os.path.exists('data'):
        os.mkdir('data')
    
    with open('data/articles.json', 'w', encoding='utf8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    asyncio.run(main())
