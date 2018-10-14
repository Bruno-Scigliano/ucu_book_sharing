from django.template.defaulttags import register


@register.filter
def get_item(dict, key):
    try:
        print(dict)
        print(key)
        return dict[key]
    except KeyError:
        return ''
