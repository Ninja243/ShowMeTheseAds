#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import time
import sys
try:
    import requests
except ImportError:
    raise ImportError(
        "This script requires the module 'requests'. Try 'pip install requests' in your command line.")

jobs = [
    'model',
    'influencer',
    'advertiser'
]

places = [
    'agency',
    'house',
    'company',
    'firm',
    'photoshoot',
    'from home',
    'gym'
]

prefix = [
    'how to be',
    'how to become',
    'can I be',
    'become',
    'be in',
    'can I join'
]

suffix = [
    'near me',
    'on Snapchat',
    'on WhatsApp',
    'on Instagram',
    'on Facebook',
    'payment',
    'get paid'
]

number_of_requests = 0

while True:
    time.sleep(random.randint(1, 6))
    query = random.choice(prefix)+" "+random.choice(jobs) + \
        " "+random.choice(places)+" "+random.choice(suffix)
    padding = " "*10
    number_of_requests += 1
    out = "\rSearch "+str(number_of_requests) + \
        " for \"%s\" completed" % query+padding
    out = out[:30]
    sys.stdout.write("\rSearch #"+str(number_of_requests) +
                     " for \"%s\" completed (Google)" % query+padding)
    sys.stdout.flush()
    try:

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "www.google.com",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
        }
        requests.get("http://www.google.com/?client=firefox-b-d&q=%s&gws_rd=ssl" %
                     query, headers=headers)
    except (KeyboardInterrupt, SystemExit):
        print(
            "\n\t%d requests made in total. Bye!" %
            (number_of_requests)
        )
        sys.exit()
