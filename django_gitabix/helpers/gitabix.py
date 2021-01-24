from datetime import timezone, timedelta, datetime

from django.conf import settings
from pygit2 import Repository
from pygit2._pygit2 import GitError

from tests.settings import GITABIX_RUNSERVER


def branch_base(info_level=None):
    return f'{repository().head.shorthand} '


def branch_rich():
    repo = repository()
    commit_info = repo.head.target

    commit = repo.revparse_single(commit_info.hex)
    tzinfo = timezone(timedelta(minutes=commit.author.offset))
    datetime_committed = datetime.fromtimestamp(float(commit.author.time), tzinfo)
    dif = repo.diff()
    deletions = dif.stats.deletions
    files_changed = dif.stats.files_changed
    insertions = dif.stats.insertions

    combined_change = deletions + insertions

    return repo.head.shorthand, combined_change


def repository():
    repo_home = repository_home()
    try:
        return Repository(repo_home)
    except GitError:
        return f'Repository not found at {repo_home}! Use GITABIX_REPO_DIR in settings,py to set a different directory'


def repository_home():
    try:
        repo_home = settings.GITABIX_REPO_DIR
    except AttributeError:
        repo_home = '.'
    return repo_home


if GITABIX_RUNSERVER:
    print(f'branch: {branch_base()}')
