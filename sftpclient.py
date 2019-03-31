import paramiko
from sys import argv

def sftpClient(host, port, username, passw=None, keypath=None, keypass=None):
	try:
		if keypath!=None:
			key=paramiko.RSAKey.from_private_key_file(keypath, password=keypass)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host, port, username, passw, key)

		sftp = ssh.open_sftp()
		sftp.sshclient = ssh
		return sftp
	except Exception as e:
		print('An error occurred creating SFTP client: {0}: {1}'.format(e.__class__, e))	
		if sftp is not None:
			sftp.close()
		if ssh is not None:
			ssh.close()
		pass		

def main():
	#set sftpClient variables below before starting.	


	try:
		sftp = sftpClient(host=None, port=None, username='user', keypath=None, keypass=None)
		print('Connection successful!')
		sftp.close()
	except Exception as e:
		print(str(e))

if __name__ == "__main__":
	main()			
