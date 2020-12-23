#!/usr/bin/env python3
"""
youtube-backup
Completely backs up a youtube channel's page for offline
viewing with the original YouTube UI.
"""

__author__ = "butforme"
__version__ = "1.0.0"
__license__ = "MIT"

import argparse
import requests
from bs4 import BeautifulSoup

def main(args):
    print(args)
    
    CHANNEL_URL = 'https://www.youtube.com/c/CodeBullet'
    CHANNEL_URL += '/videos'

    CHANNEL_RAW = requests.get(CHANNEL_URL)
    channelparsed = BeautifulSoup(CHANNEL_RAW.content, 'html.parser')

    # TODO Remove, this is just for testing purposes    
    print(channelparsed.prettify())

    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("url", help="The url of the channel to be backed up")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
