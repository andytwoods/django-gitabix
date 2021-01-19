from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from django_gitabix.helpers.gitabix import branch_base

register = template.Library()


@register.simple_tag
def branch():
    return branch_base()


@register.simple_tag
def branchpretty():
    logo = static("img/gitlogo.svg")
    return mark_safe(f'<img style="width:12px" src="{ logo }">' + branch_base())
