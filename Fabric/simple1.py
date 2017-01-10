#!/usr/bin/python

from fabric.api import * 

env.user = 'root'
env.hosts ='172.29.10.203'
env.password = 'Closeli123'

@runs_once

def local_task():
    local("uname -a")


def remote_task():
    with cd ("data/logs"):
        run("ls -l")

