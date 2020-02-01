import requests
import random
import sys
import time

USERNAME = 'yourusername'
PASSWORD = 'yourpassword'

def login(session, email, password):
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)
    assert response.status_code == 302
    assert 'c_user' in response.cookies
    return response.cookies

if __name__ == "__main__":
    session = requests.session()
    cookies = login(session, USERNAME, PASSWORD)
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
        'on Facebook'
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
                         " for \"%s\" completed (Facebook)" % query+padding)
        sys.stdout.flush()
        try:
            response = session.get("https://www.facebook.com/search/top/?q=%s&epa=SEARCH_BOX" % query, cookies=cookies,
                                   allow_redirects=False)
        except (KeyboardInterrupt, SystemExit):
            print(
                "\n\t%d requests made in total. Bye!" %
                (number_of_requests)
            )
            sys.exit()
