#!/usr/bin/env python
import sys


def main(*args):
    import api

    api.get_areas()


if __name__ == "__main__":
    main(sys.argv)
