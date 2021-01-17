from django import template
from pygit2 import Repository, GitError
from django.conf import settings

register = template.Library()


def repository_home():
    try:
        repo_home = settings.GITABIX_REPO_DIR
    except AttributeError:
        repo_home = '.'

    return repo_home


@register.simple_tag
def branch():
    repo_home = repository_home()
    try:
        return Repository(repo_home).head.shorthand
    except GitError:
        return f'Repository not found at {repo_home}! Use GITABIX_REPO_DIR in settings,py to set a different directory'
