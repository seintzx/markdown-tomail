#!/usr/bin/env python3

import configparser


def get_config(args):
    config = configparser.ConfigParser()
    config.read("config.txt")
    password = config.get("configuration", "password")
    sender_email = config.get("configuration", "sender")
    customer = config.get("configuration", "customer")
    receiver_email = ""

    if args.me:
        receiver_email = sender_email
    elif args.zoff:
        receiver_email = config.get("configuration", "receiver")
    else:
        print("Error!")

    conf = {
        'password': password,
        'sender': sender_email,
        'receiver': receiver_email,
        'customer': customer
    }
    return (conf)
