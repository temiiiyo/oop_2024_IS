class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.sections = []
        self.articles = []

    def apply(self, section):
        section.add_student(self)
        self.sections.append(section)

    def submit_article(self, article):
        self.articles.append(article)
        print(f"{self.name} подал статью: {article.title}")