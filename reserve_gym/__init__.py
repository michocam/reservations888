import requests
import json
from datetime import datetime
from datetime import timedelta
import logging
import azure.functions as func

from .x import x
#from x import x

def main(mytimer: func.TimerRequest) -> None:
    #def main():
    if mytimer.past_due:
        logging.info('The timer is past due!')

    EndDate = datetime.today() + timedelta(days=2)
    weekday = EndDate.weekday()
    date = EndDate.strftime('%-m/%-d/%Y')
    
    emailx = 'mich.ocampo@outlook.com'
    hourx = '1:00'
    z = x(weekday, date, emailx, hourx)

    emailx = 'selenelilian@hotmail.com'
    hourx = '0:30'
    z = x(weekday, date, emailx, hourx)

    logging.info(z)
    #return z
    #main()