#!/usr/bin/env python3

import urllib.request
import json
import smtplib
page = urllib.request.urlopen('https://api.greenhouse.io/v1/boards/discord/jobs')

data = str(page.read()).upper()

if 'FRONT' in data:

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('aykeri.zero@gmail.com', 'MY SECRET PASSWORD')

    smtpObj.sendmail(
        'aykeri.zero@gmail.com',
        'songya@umich.edu',
        'Subject: Discord Has Internships Open\nThis is a message from your '
        'AWS instance\n\nThe word intern has been spotted in the discord api. '
        'Hurry up and apply.')

    smtpObj.quit()
