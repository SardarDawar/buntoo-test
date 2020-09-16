from django import template
from ..models import Friend_List
register = template.Library()

@register.filter('break')
def break_(value,id):
    
    instance  =  Friend_List.objects.get(user=id)
    try:
        print(value)
        instance.friend_name.get(username=(value))
        return True
    except:
        return False
