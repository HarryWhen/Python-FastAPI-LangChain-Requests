#!/usr/bin/env python
import sys

NAME = "name"


def main(*args):
    import api

    vacancies = api.get_vacancies()
    print(f"{len(vacancies)} vacancies:")
    for vacancy in vacancies:
        print(vacancy[NAME])


if __name__ == "__main__":
    main(sys.argv)
