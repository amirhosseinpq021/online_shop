from django import template
register = template.Library()


@register.filter
def only_active_comment(comments):
    return comments.filter(is_active=True)