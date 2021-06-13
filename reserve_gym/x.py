import requests
import json
from datetime import datetime
from datetime import timedelta

import logging
import azure.functions as func

from .payload_calc import payload_calc
from .schedule import schedule

#from payload_calc import payload_calc
#from schedule import schedule

def x(weekday, date, emailx, hourx):
    if weekday == 5 or weekday == 6:
        availability = ['08:30','09:00','09:30','10:00','10:30']
        for time in availability:
            pload = payload_calc(time, date, hourx)
            res = schedule(pload, emailx)
            try:
                res_decode = res.decode("utf-8")
                res_dict = json.loads(res_decode)
                status = res_dict['success']
            except:
                status = 'failed to post'
                print('failed to post')
                
            if status == True:
                print(time, 'stop loop because of success', 'weekend')
                break
            else:
                print(time, 'try next loop', pload)
    else:
        availability = ['07:00','08:00','17:30','18:00','18:30']
        for time in availability:
            pload = payload_calc(time, date, hourx)
            res = schedule(pload, emailx)
            try:
                res_decode = res.decode("utf-8")
                res_dict = json.loads(res_decode)
                status = res_dict['success']
            except:
                status = 'failed to post'
                print('failed to post')
            
            if status == True:
                print(time, 'stop loop because of success', 'week day')
                break
            else:
                print(time, 'try next loop', pload)
    return status
