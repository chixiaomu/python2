#!/usr/bin/python

from fabric.api import *

env.user='root'
env.hosts=['172.29.10.202', '172.29.10.203']
env.password='Closeli123'

@runs_once
def input_raw():
    return prompt("please input directort name:", default="/home")

def worktask(dirname):
    run("ls -l "+dirname)

@task

def go():
    getdirname = input_raw()
    worktask(getdirname)
