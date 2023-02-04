# -*- coding: utf-8 -*-
from django import template
import datetime

register = template.Library()

@register.filter
def int2date(value):
    """Removes all values of arg from the given string"""
    dt = datetime.datetime.fromtimestamp(value/1000)
    formatedDate = dt.strftime("%Y-%m-%d")
    return formatedDate

@register.filter
def getdays(pdate, ndate):
    return 1.0*(ndate-pdate)/(24*60*60*1000)

@register.filter
def subtract(value, arg):
    return value - arg