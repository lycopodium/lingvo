import tonality
import json

def main():
    with open('data/articles.json', 'r', encoding='utf8') as f:
        articles = json.load(f)
        articles_tonality = []
        for article in articles:
            sentences = article['text'].split('.')
            ton = tonality.predict(sentences)
            article_tonality = {
                'article_id': article['id'],
                'tonalities': ton
            }
            articles_tonality.append(article_tonality)

        with open('data/tonality.json', 'w') as f2:
            json.dump(articles_tonality, f2, indent=4)



if __name__ == "__main__":
    main()
            