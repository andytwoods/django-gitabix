from django.conf import settings
from pygit2 import Repository
from pygit2._pygit2 import GitError

from tests.settings import GITABIX_RUNSERVER

def branch_base():
    repo_home = repository_home()
    try:
        return Repository(repo_home).head.shorthand
    except GitError:
        return f'Repository not found at {repo_home}! Use GITABIX_REPO_DIR in settings,py to set a different directory'


def repository_home():
    try:
        repo_home = settings.GITABIX_REPO_DIR
    except AttributeError:
        repo_home = '.'
    return repo_home


if GITABIX_RUNSERVER:
    print(f'branch: { branch_base() }')
