from django import template
import datetime
import re
from django.utils import timesince

"""
   Alternate form of Django's "timesince" that shortens the dates to a single letter. 
"""
register = template.Library()
def dtsince(value):
    # "4 hours, 1 minute" --> "4h, 1m"
    dt_init = timesince.timesince(value)
    dt_b = re.sub(r'\sminute(s|)(,|)', 'm\g<2>', dt_init)
    dt_b = re.sub(r'\shour(s|)(,|)', 'h\g<2>', dt_b)
    dt_b = re.sub(r'\sday(s|)(,|)', 'd\g<2>', dt_b)
    dt_b = re.sub(r'\sweek(s|)(,|)', 'w\g<2>', dt_b)
    dt_b = re.sub(r'\smonth(s|)(,|)', 'mo\g<2>', dt_b)
    dt_b = re.sub(r'\syear(s|)(,|)', 'y\g<2>', dt_b)
    return dt_b;

register.filter("dtsince",dtsince)
