class GetSpouses:
    def __init__(self, person):
        self.person = person

    def run(self, prolog):
        query = f"marriage({self.person}, Spouse, _, _); marriage(Spouse, {self.person}, _, _)."
        results = prolog.query(query)
        if results:
            spouses = [r["Spouse"] for r in results]
            print(f"Супруг(и) {self.person}: {', '.join(spouses)}")
        else:
            print(f"У {self.person} нет супругов в базе")
