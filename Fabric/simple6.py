#!/usr/bin/python

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

import time


env.user='root'
env.hosts=['172.29.10.202', '172.29.10.203']
env.password='Closeli123'


env.project_dev_source = '/data/dev/Lwebadmin/'
env.project_tar_source = '/data/dev/releases/'
env.project_pack_name = 'release'

env.deploy_project_root = '/data/www/Lweadmin/'
env.deploy_release_dir = 'releases'
env.deploy_current_dir = 'current'
env.deploy_version = time.strftime("%Y%m%d")+"v2"

@runs_once
def input_versionid():
    return prompt("please input project roollback version ID:', default="")
