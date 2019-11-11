#!/usr/bin/env python3

import argparse


def param():
    parser = argparse.ArgumentParser(
        description="choose the recipient of the mail")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-m",
                       "--me",
                       help="send mail to yourself (test purpose)",
                       action="store_true")
    group.add_argument("-b",
                       "--boss",
                       help="send mail to boss",
                       action="store_true")

    return (parser.parse_args())
