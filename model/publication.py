import datetime

class Publication:
    id:int
    title: str
    journal: str
    pub_date: datetime.datetime

    def __init__(self, id, title, pub_date, journal):
        self.id = id
        self.title = title
        self.pub_date = pub_date
        self.journal = journal


    def show(self):
        print(f"id={self.id}, title={self.title}, pubdate={self.pub_date}, journal={self.journal}")
