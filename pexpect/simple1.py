#!/usr/bin/python

from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('please input password: ')
    s.login (hostname, username, password)
    s.sendline('pwd')
    s.prompt()
    print s.before

    s.sendline(' ls -l')
    s.prompt()
    print s.before

    s.sendline(' df ')
    s.prompt()
    print s.before
except pxssh.ExceptionPxssh, e:
    print "pxssh faild on login."
    print str(e)
