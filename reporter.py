#!/usr/bin/env python3

import pypandoc
import os


def md_convert(path):
    pypandoc.convert_file(path, 'html', outputfile="body.html")


def create(customers, path):
    if not os.path.isfile(path):
        try:
            f = open(path, "w+")
            for customer in customers:
                f.write("**{0}**\n\n".format(customer) + \
                         "*Incidenti Rilevanti*\n\n" + \
                         "*Attività in Corso*\n\n")
        except Exception as e:
            print(str(e))
        finally:
            f.close()
