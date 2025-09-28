class GetGrandparents:
    def __init__(self, person):
        self.person = person

    def run(self, prolog):
        query = f"grandparent(GP, {self.person})."
        results = prolog.query(query)
        if results:
            gps = [r["GP"] for r in results]
            print(f"Дедушки и бабушки {self.person}: {', '.join(gps)}")
        else:
            print(f"У {self.person} нет дедушек и бабушек в базе")
