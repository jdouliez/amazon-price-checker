# pylint: disable=missing-function-docstring
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import sub
from decimal import Decimal
import smtplib
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import requests


####### CONFIG ########

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_LOGIN = ""
SMTP_PWD = ""

EMAIL_FROM = "price-checker@amazon.fr"
EMAIL_TO =  ""

DEBUG = False
#######################


def check_price():
    global DEBUG

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find(id='twister-plus-price-data-price').get('value').strip()

    now = datetime.now()

    if DEBUG:
        print("[+] Current price : " + str(price) + "€" +  " - " + now.strftime("%d/%m/%Y %H:%M:%S"))

    if int(price) < int(PRICE):
        if DEBUG:
            print('[+] Sending email')

        send_email(title, price, URL)


def send_email(title, price, url):
    global DEBUG

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_LOGIN, SMTP_PWD)

    subject = "Amazon : Prix interessant !"
    body = f"Le \"{title}\" est à {price}€ (URL : {url}) "
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.encode("utf8"))

    if DEBUG:
        print('[+] An e-mail has been sent to ' + EMAIL_TO + '!')

    server.quit()


URL = sys.argv[1]
PRICE = sys.argv[2]

if __name__ == "__main__":
    if DEBUG:
        print('[+] Analyzing url ' + URL)
        print('[+] Checking if price is lower than ' + PRICE)

    check_price()


