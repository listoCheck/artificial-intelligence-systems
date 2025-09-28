class MarriedLongerThan:
    def __init__(self, person1, person2, years):
        self.person1 = person1
        self.person2 = person2
        self.years = years

    def run(self, prolog):
        query = f"married_longer_than({self.person1}, {self.person2}, {self.years})."
        results = prolog.query(query)
        if results:
            print(f"{self.person1} и {self.person2} были женаты дольше {self.years} лет")
        else:
            print(f"{self.person1} и {self.person2} не были женаты дольше {self.years} лет")
