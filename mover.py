import shutil, os, sys

class move_paper:
	
	def __init__(self):
		self.root = sys.argv

	def cli(self):
		if len(self.root) < 2:
			return False
		else:
			return True

	def mover(self):
		count = 0
		for root, direct, files in os.walk(self.root[1]):
			#print(root)

			for name1 in files:
				
				src = os.path.join(root, name1)
				
				dest = os.path.join(self.root[1], str(count)+name1)	
				spl = os.path.splitext(dest)
				count += 1
				if not os.path.isfile(dest) and spl[1]==".jpg":	
					shutil.move(src, dest)
					print(dest)
				else:
					print("Not moved")				
		print(count)			
	def main(self):
	
		enough = self.cli()

		if enough:
			self.mover()
		else:
			print("Please provide a path for directory to begin")	



mp = move_paper()
mp.main()