import os
from subprocess import check_output
import webbrowser
from django.http import JsonResponse


def action(request):
    url = 'pycharm://open?file=/Users/andytwoods/django-gitabix/django_gitabix/apps.py'
    webbrowser.open(url, new=0, autoraise=True)
    #window.open('pycharm://open?file=file_path', '_top')
    return JsonResponse({})
