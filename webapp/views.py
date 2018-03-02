from django.shortcuts import render
from django.http import  HttpResponse
from subprocess import Popen, PIPE
from os import path

def index(request) :
    git_command = ['/usr/bin/git', 'status']
    repository = path.dirname('/home/cp/Desktop/code/git/django-tut/learn-django/')
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()
    if git_query.poll() == 0:
        print(git_status)

    return HttpResponse("<h2>Hola!</h2>"+str(git_status, 'utf-8'))
