class Collection:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def publish(self):
        print("Сборник публикаций:")
        for article in self.articles:
            print(f"- {article.title}")