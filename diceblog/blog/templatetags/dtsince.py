from django import template

register = template.Library()

def dtsince(value):
    return "0h";

register.filter("dtsince",dtsince)
