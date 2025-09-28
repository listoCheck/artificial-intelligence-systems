class IsMarried:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def run(self, prolog):
        query = f"marriage({self.person1}, {self.person2}, Start, End)."
        results = prolog.query(query)
        if results:
            print(f"{self.person1} и {self.person2} состоят в браке")
        else:
            print(f"{self.person1} и {self.person2} не состоят в браке")
