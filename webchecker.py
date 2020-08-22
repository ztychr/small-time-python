import requests
import sys
import os

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
	print 'Usage: python webchecker.py [ip-1 ip-2 ip-n]'
	sys.exit(0)

for arg in sys.argv[1:]:
	try:
		r1 = requests.get('http://' + arg, timeout=5)
		print arg, 'PORT  80:', r1.status_code

		if r1.status_code == 200:
			with open (sys.argv[1] + '.txt', 'a') as scope:
				scope.write(arg + ' - P80\n')

		elif r1.status_code == 400:
			with open (sys.argv[1] + '.txt', 'a') as scope:
                        	scope.write(arg + r1.status_code + ' - P80\n')

	except requests.Timeout:
		print arg, 'PORT  80: Timeout'
	except requests.ConnectionError:
		print arg, 'PORT  80: Connection refused. Possibly open.'
	except requests.RequestException as e:
		print arg, 'PORT  80', e


        try:
                r2 = requests.get('https://' + arg, timeout=5)
                print arg, 'PORT 443:', r2.status_code

                if r2.status_code == 200:
                        with open (sys.argv[1] + '.txt', 'a') as scope:
                                scope.write(arg + ' - P443\n')

                elif r2.status_code == 400:
                        with open (sys.argv[1] + '.txt', 'a') as scope:
                                scope.write(arg + r2.status_code + ' - P443\n')

        except requests.Timeout:
                print arg, 'PORT 443: Timeout'
        except requests.ConnectionError:
                print arg, 'PORT 443: Connection refused. Possibly open.'
        except requests.RequestException as e:
                print arg, 'PORT 443', e

