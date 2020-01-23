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


## TABLE VERSION


def create_html(customers, path):
    if not os.path.isfile(path):
        try:
            f = open(path, "w+")
            for customer in customers:
                f.write("<b>{0}</b>".format(customer) + "||\n")
        except Exception as e:
            print(str(e))
        finally:
            f.close()


def make_table(path, output_file):
    try:
        f = open(path, 'r')
        content = f.readlines()
    except Exception as e:
        print(str(e))
    finally:
        f.close()

    rows = []
    for c in content:
        cells = c.split('|')
        cells = ['<td>{}</td>'.format(cell.strip()) for cell in cells]
        rows.append(cells)
    try:
        f = open(output_file, 'w+')
        f.write('<table border=1>\n')
        for r in rows:
            f.write('<tr>\n')
            for c in r:
                f.write('    {}\n'.format(c))
            f.write('</tr>\n')
        f.write('\n</table>')
    except Exception as e:
        print(str(e))
    finally:
        f.close()
