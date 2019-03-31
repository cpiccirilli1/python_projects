import zipfile, sys

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd =password)
		return password
	except:
		return

def main():
	zFile = zipfile.ZipFile('evil.zip')
	with open('dictionary.txt', 'r') as dct:
		for line in dct:
			password = line.strip()
			guess = extractFile(zFile, password)
			if guess:
				print('[+] Password = ' +password +'\n')
				sys.exit(0)

if __name__ == "__main__":
	main()							