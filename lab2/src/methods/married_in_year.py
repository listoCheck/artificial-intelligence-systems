class MarriedInYear:
    def __init__(self, person1, person2, year):
        self.person1 = person1
        self.person2 = person2
        self.year = year

    def run(self, prolog):
        query = f"married_in_year({self.person1}, {self.person2}, {self.year})."
        results = prolog.query(query)
        if results:
            print(f"{self.person1} и {self.person2} были женаты в {self.year} году")
        else:
            print(f"{self.person1} и {self.person2} не были женаты в {self.year} году")
