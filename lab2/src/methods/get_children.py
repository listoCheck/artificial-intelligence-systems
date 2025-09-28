class GetChildren:
    def __init__(self, parent):
        self.parent = parent

    def run(self, prolog):
        query = f"parent({self.parent}, Child, _)."
        results = prolog.query(query)
        if results:
            children = [r["Child"] for r in results]
            print(f"Дети {self.parent}: {', '.join(children)}")
        else:
            print(f"У {self.parent} нет детей в базе")
