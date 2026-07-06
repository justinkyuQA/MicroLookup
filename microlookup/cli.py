import sys

from .core import lookup

HELP = """
MicroLookup v0.1

Usage

python3 -m microlookup <hostname>

Example

python3 -m microlookup google.com
"""

def main():

    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    lookup(args[0])
