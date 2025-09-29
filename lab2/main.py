import logging
import re

from swiplserver import PrologMQI, create_posix_path

from lab2.src.methods.get_children import GetChildren
from lab2.src.methods.get_grandparents import GetGrandparents
from lab2.src.methods.get_parents import GetParents
from lab2.src.methods.get_siblings import GetSiblings
from lab2.src.methods.get_spouses import GetSpouses
from lab2.src.methods.get_uncles_aunts import GetUnclesAunts
from lab2.src.methods.is_alive import IsAlive
from lab2.src.methods.is_married import IsMarried
from lab2.src.methods.married_in_year import MarriedInYear
from lab2.src.methods.married_longer_than import MarriedLongerThan
from src.methods import (
    get_parents, get_children, get_siblings, get_grandparents,
    is_alive, is_married, married_longer_than, get_uncles_aunts,
    married_in_year, get_spouses
)

KNOWLEDGE_BASE_PATH = "../lab1/baze.pl"

incorrect_request = "Неправильный запрос"

requests = [
    "Кто родители liza_m?",
    "Кто дети у andrey_v?",
    "Кто братья и сестры у kate_a?",
    "Кто дедушки и бабушки у artem_a?",
    "Жив ли vladimir_n в 1980 году?",
    "Жива ли galina_k в 2025 году?",
    "Состоят ли elena_e и andrey_v в браке?",
    "Были ли olga_v и mark_a в браке дольше 20 лет?",
    "Кто дяди или тети у liza_m?",
    "Были ли dina_d и eduard_a женаты в 1965 году?",
    "Кто супруги у elena_k?",
]

patterns = {
    r"Кто родители (.+)\?": GetParents,
    r"Кто дети у (.+)\?": GetChildren,
    r"Кто братья и сестры у (.+)\?": GetSiblings,
    r"Кто дедушки и бабушки у (.+)\?": GetGrandparents,
    r"Жив ли (.+) в (\d+) году\?": IsAlive,
    r"Жива ли (.+) в (\d+) году\?": IsAlive,
    r"Состоят ли (.+) и (.+) в браке\?": IsMarried,
    r"Были ли (.+) и (.+) в браке дольше (\d+) лет\?": MarriedLongerThan,
    r"Кто дяди или тети у (.+)\?": GetUnclesAunts,
    r"Были ли (.+) и (.+) женаты в (\d+) году\?": MarriedInYear,
    r"Кто супруги у (.+)\?": GetSpouses,
}


def start() -> None:
    logging.getLogger().setLevel(logging.WARNING)

    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog:
            path = create_posix_path(KNOWLEDGE_BASE_PATH)
            logging.debug("DEBUG: knowledge base path %s", path)

            prolog.query(f'consult("{path}")')
            logging.debug("DEBUG: knowledge base loaded")

            print("\nПримеры запросов, которые вам доступны:")
            print(" * " + "\n * ".join(requests))
            print("\nДля завершения введите - exit.\n")

            while True:
                query = input("> ")
                if query.lower() == "exit":
                    break

                for pattern in patterns:
                    match = re.match(pattern, query, re.IGNORECASE)
                    if match is None:
                        continue

                    processor = patterns[pattern](*match.groups())
                    processor.run(prolog)
                    break
                else:
                    print(incorrect_request)


if __name__ == "__main__":
    start()
