from django import template
from django.template import loader
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from django_gitabix.helpers.gitabix import branch_base, branch_rich

register = template.Library()


@register.simple_tag
def branch():
    return branch_base()


@register.simple_tag
def branchpretty():
    logo = static("django_gitabix/gitlogo.svg")

    basic_info, combined_change = branch_rich()
    combined_change_visual = gen_icon(static("django_gitabix/bix.png"), 6)
    combined_change_visual = ''.join([combined_change_visual for _ in range(combined_change)])
    combined_change_visual = f"<span style='margin-left:5px;'>{combined_change_visual}</span>"
    return mark_safe(f'<div><img style="width:12px" src="{ static("django_gitabix/gitlogo.svg") }">'
                     + basic_info + combined_change_visual+ '</div>')

GITABIX_COOKIE_SLEEP = 'gitabix_cookie_sleep'

@register.simple_tag(takes_context=True)
def branchpretty2(context):
    t = loader.get_template('django_gitabix/gitabixpretty.html')
    print(context['request'].COOKIES)
    if context['request'].COOKIES.get(GITABIX_COOKIE_SLEEP, 0) == '1':
        return t.render({'hidden': True, 'GITABIX_COOKIE_SLEEP': GITABIX_COOKIE_SLEEP})
    basic_info, combined_change = branch_rich()
    return t.render({'basic_info': basic_info,
                     'changes': range(combined_change),
                     'hidden': False,
                     'GITABIX_COOKIE_SLEEP': GITABIX_COOKIE_SLEEP})

def gen_icon(logo: str, width: int=12):
    return f'<img style="width:{width}px" src="{logo}" alt="biscuit"    >'
