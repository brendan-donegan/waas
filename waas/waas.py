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
    parser.add_argument(
        '--units',
        help="Unit system to use.",
        choices=['metric','imperial'],
        default='metric'
    )
    args = parser.parse_args()
    print(get_current_weather(ip=args.ip, units=args.units))


if __name__ == "__main__":
    sys.exit(main())
