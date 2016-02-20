#!/usr/bin/env python

import sys
import pprint

from argparse import ArgumentParser

from weather import get_current_weather

def main():
    parser = ArgumentParser("Weather forecast")
    parser.add_argument(
        "--ip", 
        help="IP address to get weather for. Uses "
        "your own IP address if not specified."
    )
    args = parser.parse_args()
    print(get_current_weather(args.ip))


if __name__ == "__main__":
    sys.exit(main())
