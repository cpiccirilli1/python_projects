import re, sys, os

class regtest:
	def __init__(self, args):
		self.dir = args

	def reg(self):
		three_bracket = re.compile(r"(\[.*?\]\s)(.*?)(\[.*?\])(\[.*?\])")
		two_bracket = re.compile(r'(\[.*?\]\s)(.*?)(\[.*?\])')
		#ne_par = compile(r"")
		#two_par = compile(r"")

		return three_bracket, two_bracket

	def sledge(self):
		three, two = self.reg()
		two_list, three_list = self.count()
		file_list = os.listdir(self.dir)
		fixed = list()

		if two_list:
			for t, f in zip(two_list, file_list):
				if t == f:
					begin, end = os.path.splitext(t)
					filename = two.findall(begin)
					fixed.append(filename)

		if three_list:
			for t, f in zip(three_list, file_list):
				if t == f:
					begin, end = os.path.splitext(t)
					filename = three.findall(begin)
					fixed.append(filename)

		
		for fix in fixed:
			print(fix[0])											



	def count(self):
		
		file_list = os.listdir(self.dir)	
		two_list = list()
		three_list = list()

		for f in file_list:
			name, ext = os.path.splitext(f)
			count = 0
			if ext in '.mkv':
				for n in name:
					if n == "[":
						count +=1

			if count == 2:
				two_list.append(f)
			elif count == 3:
				three_list.append(f)
			else:
				pass

		return two_list, three_list		

			
def main():
	path = os.path.join(os.path.expanduser("~"), "Documents", "torrents")
	test = regtest(path)
	test.sledge()

if __name__ == "__main__":
	main()		