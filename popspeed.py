#!/usr/bin/env python

# All your bugreports and ehnancement requests belong to frontman@gmail.com

import sys,os, poplib, imaplib
from datetime import datetime, timedelta
from decimal import Decimal
import signal

def show_usage():
	print "Usage:\n popspeed $server $user $pass"
	sys.exit()

def bye (signum, sf):
	print "\nBye!"
	sys.exit()

def POP3Connect (host, user, passwd, port=110):
	if not port: port = 110
	conn = poplib.POP3(host,port)
	conn.user  (user)
	conn.pass_ (passwd)
	return conn

signal.signal(signal.SIGINT, bye)
signal.signal(signal.SIGHUP, bye)

if not len(sys.argv) ==4:
	show_usage()

(host, user, passwd) = sys.argv[1:4]

print "Trying to connect to %s@%s via POP3" % (user, host)

conn = POP3Connect (host, user, passwd)
numMessages = len(conn.list()[1])

if numMessages == 0:
	print "0 Messages found in the mailbox, aborting..."
	sys.exit()

print "Found %d messages, starting download..." % numMessages

for id in range (numMessages):
	start = datetime.now()
	mess = conn.retr(id+1)[1]
	dl_time = datetime.now() - start	
	size = len(''.join(mess))

	size_kb = Decimal(size)/(1024)		# size in KB
	dl_sec = Decimal(dl_time.seconds) + Decimal(dl_time.microseconds)/10**6 	# download time in seconds
	avg_speed = size_kb / dl_sec 		# average speed for the download
	
	print "Message %d: DL time: %.2fs, size:%.2f KB, AVG Speed: %.2f KB/s" % (id+1,dl_sec,size_kb,avg_speed)

print 'Done.'
	
