from django.conf import settings
from pygit2 import Repository
from pygit2._pygit2 import GitError

from tests.settings import GITABIX_RUNSERVER

RICH = 'rich info'

def branch_base(info_level=None):
    repo_home = repository_home()
    try:
        repository = Repository(repo_home)
        if not info_level:
            return repository.head.shorthand
        if info_level is RICH:
            commit_info = repository.head.target
            commit = repository.revparse_single
            print(commit.author.time)
            return f'{repository.head.shorthand} '

    except GitError:
        return f'Repository not found at {repo_home}! Use GITABIX_REPO_DIR in settings,py to set a different directory'


def repository_home():
    try:
        repo_home = settings.GITABIX_REPO_DIR
    except AttributeError:
        repo_home = '.'
    return repo_home


if GITABIX_RUNSERVER:
    print(f'branch: { branch_base(RICH) }')
