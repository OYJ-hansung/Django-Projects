from django import template

register = template.Library() #default setting

@register.filter(name='myAppend')
def custAppend(value, arg):
    result = str(arg)+ value
    return result

@register.filter(name='myLower')
def custLower(value):
    value_list = list(value)
    length = len(value)
    if length > 3:
        for idx in range(3):
            value_list[idx] = value_list[idx].lower()
        return ''.join(value_list)
    else:
        return value.lower()
    

