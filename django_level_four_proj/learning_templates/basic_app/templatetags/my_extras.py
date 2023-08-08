from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,arg):
    """
    this is cut value of args from string
    """
    return value.replace(arg, '')
