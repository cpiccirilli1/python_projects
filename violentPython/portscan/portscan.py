import optparse, sys, socket
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def main():
	parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')

	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = str(options.tgtPort).split(', ')
	
	if (tgtHost == None) | (tgtPort[0] == None):
		print(parser.usage)
		sys.exit(0)
	portScan(tgtHost, tgtPort)	

def connScan(tgtHost, tgtPort):
	try:	
		connSock = socket(AF_INET, SOCK_STREAM)
		connSock.connect((tgtHost, tgtPort))
		connSock.send('Blarg\r\n')
		results = connSock.recv(100)
		screenLock.acquire()
		print('[+] %d/tcp open' % tgtPort)
		print('[+] '+str(results))
	except:
		screenLock.acquire()
		print('[-] %d/tcp closed' % tgtPort)
	finally:
		screenLock.release()
		connSock.close()	

def portScan(tgtHost, tgtPorts):	
	try:
		tgtIP = gethostbyname(tgtHost)	
	except:
		print('[-] Cannot resolve "%s": Unknown host' % tgtHost)
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print('\n[+] Scan Results for: '+ tgtName[0])
	except:
		print('\n[+] Scan Results for: ' +tgtIP)
	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		r = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		r.start()

if __name__ == '__main__':
	main()