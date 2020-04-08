#!/usr/bin/env python

import re
import sys
import json

def arg(argv,a):
	if a in argv:
		return argv[argv.index(a)+1]

def read_ip():
	f = open('ssh.centos.tmp','r')
	s = re.sub(r'.*@','',f.read())[:-1]
	f.close()
	return s

mode = None
hostname = None
if '--list' in sys.argv:
	mode = 'list'
elif '--host' in sys.argv:
	mode = 'host'
	hostname = arg(sys.argv,'--host')

ob = None
try:
	if mode == 'list':
		ob = {
			'elasticsearch': {
				'hosts':[read_ip()],
				'vars':{
					'ansible_ssh_key':'~/.ssh/ec2key1.pem',
					'ansible_ssh_user':'centos'
				}
			}
		}
		ob['prometheus'] = ob['elasticsearch']
	
	elif mode == 'host':
		ob = {}

except Exception as e:
	# Do something here, I guess...
	raise e
finally:
	print json.dumps(ob,indent=2)




