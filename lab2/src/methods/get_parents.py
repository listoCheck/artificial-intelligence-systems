class GetParents:
    def __init__(self, child):
        self.child = child

    def run(self, prolog):
        query = f"parent(Parent, {self.child}, _)."
        results = prolog.query(query)
        if results:
            parents = [r["Parent"] for r in results]
            print(f"Родители {self.child}: {', '.join(parents)}")
        else:
            print(f"У {self.child} нет родителей в базе")
