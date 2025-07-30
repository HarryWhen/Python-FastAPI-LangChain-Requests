#!/usr/bin/env python
import sys
from operator import itemgetter


class Config:
    DEBUG = True


def report_vacancies(vacancies):
    yield (f"{len(vacancies)} vacancies:")
    yield from map(itemgetter("name"), vacancies)


def main(*args):
    import hh_api

    vacancies = hh_api.get_vacancies()
    with open(".run_output.txt", "w") as output:
        output.writelines(map("{}\n".format, report_vacancies(vacancies)))


if __name__ == "__main__":
    main(sys.argv)
