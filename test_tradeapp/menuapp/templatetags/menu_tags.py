from django import template
from menuapp.models import MenuItem

register = template.Library()


@register.inclusion_tag('menuapp/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(
        name=menu_name).select_related('parent')
    return {'menu_items': menu_items, 'request': request}
