class Drug:
    id: str
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        print(f"id={self.id}, name={self.name}")
