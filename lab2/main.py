import logging
import re

from swiplserver import PrologMQI, create_posix_path
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
    r"Кто родители (.+)\?": get_parents,
    r"Кто дети у (.+)\?": get_children,
    r"Кто братья и сестры у (.+)\?": get_siblings,
    r"Кто дедушки и бабушки у (.+)\?": get_grandparents,
    r"Жив ли (.+) в (\d+) году\?": is_alive,
    r"Жива ли (.+) в (\d+) году\?": is_alive,
    r"Состоят ли (.+) и (.+) в браке\?": is_married,
    r"Были ли (.+) и (.+) в браке дольше (\d+) лет\?": married_longer_than,
    r"Кто дяди или тети у (.+)\?": get_uncles_aunts,
    r"Были ли (.+) и (.+) женаты в (\d+) году\?": married_in_year,
    r"Кто супруги у (.+)\?": get_spouses,
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
