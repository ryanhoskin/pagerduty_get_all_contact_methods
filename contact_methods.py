#!/usr/bin/env python

import datetime
import requests
import sys

#Your PagerDuty API key.  A read-only key will work for this.
AUTH_TOKEN = '3TEqLQaY2bG7zsyzE5pD'
#The API base url, make sure to include the subdomain
BASE_URL = 'https://pdt-ryan.pagerduty.com/api/v1'

HEADERS = {
    'Authorization': 'Token token={0}'.format(AUTH_TOKEN),
    'Content-type': 'application/json',
}

def get_users():
    all_users = requests.get(
        '{0}/users'.format(BASE_URL),
        headers=HEADERS
    )
    sys.stdout.write("Listing All Users' Contact Methods:\n")
    for user in all_users.json()['users']:
        sys.stdout.write("User: ")
        sys.stdout.write(user['name'])
        sys.stdout.write("\n")
        get_contact_methods(user['id'])
        sys.stdout.write("-----\n")

def get_contact_methods(user_id):
    all_contact_methods = requests.get(
        '{0}/users/{1}/contact_methods'.format(BASE_URL,user_id),
        headers=HEADERS
    )
    for contact_method in all_contact_methods.json()['contact_methods']:
        if contact_method['type'] == 'phone':
            sys.stdout.write("Phone:  ")
            sys.stdout.write(contact_method['phone_number'])
        elif contact_method['type'] == 'SMS':
            sys.stdout.write("SMS:  ")
            sys.stdout.write(contact_method['phone_number'])
        elif contact_method['type'] == 'email':
            sys.stdout.write("Email:  ")
            sys.stdout.write(contact_method['address'])
        elif contact_method['type'] == 'push_notification':
            sys.stdout.write("Push:  ")
            sys.stdout.write(contact_method['label'])
        sys.stdout.write("\n")

get_users()