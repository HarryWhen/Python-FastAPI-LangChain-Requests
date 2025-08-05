#!/usr/bin/env python
import sys


class Config:
    DEBUG = True
    LOG = True


def main(*args):
    import response_to_vacancy

    response_to_vacancy.run()


if __name__ == "__main__":
    main(sys.argv)
