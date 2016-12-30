#!/usr/bin/python


import pexpect
import sys

ip="172.29.10.203"
user="root"
passwd="Closeli123"
target_file="/var/log/messages-20161204"

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])
fout = file('mylog.txt','w')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar zcvfP /var/log/message.tar.gz'+target_file)
    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"

child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/var/log/message.tar.gz','/home'])
fout = file('mylog.txt','a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"
