import requests
import json
from datetime import datetime
from datetime import timedelta

import logging
import azure.functions as func


def schedule(payload_create, emailx):
    s = requests.session()
    url = "https://888bellevue.activebuilding.com/login"
    payload = {'username': emailx,'password':'password'}
    response = s.post(url, data = payload)
    print('login',response.content)
    print('login response',response.status_code)
    url_create = "https://888bellevue.activebuilding.com/portal/reservations/create"
    response_create = s.post(url_create, data = payload_create)
    content = response_create.content
    print('response_ceate',response_create.status_code)
    print('response', content)
    return content
