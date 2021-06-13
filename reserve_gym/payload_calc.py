import requests
import json
from datetime import datetime
from datetime import timedelta

import logging
#import azure.functions as func

def payload_calc(time, date, hourx):
    payload_create = {'isOfficeUse': 'staff', 'amenityId': 15449, 'startDate': date, 'startTime': time, 'durationHours': hourx, 'approve-regulations': 'on'}
    print('payload',payload_create)
    return payload_create
