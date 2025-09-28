class IsAlive:
    def __init__(self, person, year):
        self.person = person
        self.year = year

    def run(self, prolog):
        query = f"alive({self.person}, {self.year})."
        results = prolog.query(query)
        if results:
            print(f"{self.person} жив(а) в {self.year} году")
        else:
            print(f"{self.person} не жив(а) в {self.year} году")
