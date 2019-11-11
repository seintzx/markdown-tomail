# Monthly report

Script for generating a monthly report with the summary of each customer

# Installation

`pip install -r requirements.txt`

## Configuration file

Create the `config.txt` file or edit the existent one
```
[configuration]
password = [google one-time app password]
sender = example@example.com
receiver = example@example.com
customer = customer1,customer2,customer3,etc..
```

# Usage

```
usage: monthly.py [-h] [-m | -b]

choose the recipient of the mail

optional arguments:
  -h, --help  show this help message and exit
  -m, --me    send mail to yourself (test purpose)
  -b, --boss  send mail to boss
```
