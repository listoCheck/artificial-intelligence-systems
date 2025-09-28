class GetUnclesAunts:
    def __init__(self, person):
        self.person = person

    def run(self, prolog):
        query = f"uncle_aunt(UncleAunt, {self.person})."
        results = prolog.query(query)
        if results:
            uncles_aunts = [r["UncleAunt"] for r in results]
            print(f"Дяди и тети {self.person}: {', '.join(uncles_aunts)}")
        else:
            print(f"У {self.person} нет дядей и тетей в базе")
