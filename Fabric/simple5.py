#!/usr/bin/python

from fabric.colors import *
from fabric.api import *

env.user='root'
env.roledefs = {
    'webserver': ['192.168.1.21', '192.268.1.22']
    'dbservers': ['192.168.1.23']
}

env.password = {
    'root@192.168.1.21:22': '12ssded'
    'root@192.168.1.22:22': 'SKJH935yft'
    'root@192.168.1.23:22': 'sk6783js'
}



@roles('webserver')
def webtask():
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install naginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")

@roles('dbservers')
def dbtask():
    print yellow("Install Mysql...")
    with settings(warn_only = True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")


@roles('webserver', 'dbserver')
def publictask():
    print yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)
