import socket

def bannerRetrieve(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner):
	bannerList = []
	with open('vulnFTP.txt', 'r') as b:
		for line in b:
			bannerList.append(line.strip())

	if banner in bannerList:
		print("[+] %s is vulnerable." % banner)
	else:
		print ('[-] %s is not vulnerable.' % banner)	

def main():
	port = [21, 22, 25, 80, 110]				
	for x in range(1,255):
		for p in port:
			ip = '192.168.95.' + str(x)
			print('[+] Checking %d:%d.' %(ip, str(p)))
			banner = bannerRetrieve(ip, p)
			checkVulns(banner)

if __name__ = '__main__':
	main()		