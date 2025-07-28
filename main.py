#!/usr/bin/env python
import sys


def main(*args):
    import hh_api

    vacancies = hh_api.get_vacancies()
    print(f"{len(vacancies)} vacancies:")
    for vacancy in vacancies:
        print(vacancy["name"])


if __name__ == "__main__":
    main(sys.argv)
