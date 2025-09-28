class GetSiblings:
    def __init__(self, person):
        self.person = person

    def run(self, prolog):
        query = f"sibling({self.person}, Sibling)."
        results = prolog.query(query)
        if results:
            siblings = [r["Sibling"] for r in results]
            print(f"Братья и сестры {self.person}: {', '.join(siblings)}")
        else:
            print(f"У {self.person} нет братьев и сестер в базе")
