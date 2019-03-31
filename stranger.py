import os, shutil
path = '/media/seachel/Kindle/documents/'
path2 = '/home/seachel/Documents/ebooks/'
for root, sub, fName in os.walk(path):

	for f in fName:
		
		shutil.move(os.path.join(path, root, f), os.path.join(path2, f))
		#print('{0} is the folder: {1} is the file.'.format(root, f))
			