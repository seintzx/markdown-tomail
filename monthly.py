#!/usr/bin/env python3
"""
WorkFlow: md to html, send mail, create new md

NOTE: Must be launched on the new month
"""

import configuration
import dater
import mailer
import parameters
import reporter


def main():
    cred = configuration.get_config(parameters.param())

    customer = cred['customer'].split(",")
    del cred['customer']

    old_nmonth = dater.get_date()[1]
    new_nmonth = dater.get_date()[3]
    curr_nyear = dater.get_date()[4]

    subject = "[Monthly Summary] {0} {1} - Andrea Casadei".format(
        curr_nyear, old_nmonth)
    old_report = "report/monthly-report-{0}-{1}.md".format(
        curr_nyear, old_nmonth)
    new_report = "report/monthly-report-{0}-{1}.md".format(
        curr_nyear, new_nmonth)

    # reporter.md_convert(old_report)

    ## TABLE VERSION
    reporter.make_table(old_report, "body.html")

    try:
        sig = open('signature.html', 'r')
        txt = open('body.html', 'r')
        signature = sig.read()
        text = txt.read()
    except Exception as e:
        print(str(e))
    finally:
        sig.close()
        txt.close()
    body = "Ciao Zoff,<br>" + \
           "<html> <body>" + \
           "{0}".format(text) + \
           "<br> <br> Saluti,<br>" + \
           "{0}".format(signature) + \
           "</body> </html>"

    mailer.send(cred, subject, body)
    # reporter.create(customer, new_report)

    ## TABLE VERSION
    reporter.create_html(customer, new_report)


if __name__ == "__main__":
    main()
