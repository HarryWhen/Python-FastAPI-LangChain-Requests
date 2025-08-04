#!/usr/bin/env python
import sys
from operator import itemgetter


class Config:
    DEBUG = True


def report_vacancies(vacancies):
    yield (f"{len(vacancies)} vacancies:")
    yield from map(itemgetter("name"), vacancies)


def main(*args):
    import response_to_vacancy

    response_to_vacancy.run()


if __name__ == "__main__":
    main(sys.argv)
