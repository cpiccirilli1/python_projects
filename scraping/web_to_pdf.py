from bs4 import BeautifulSoup as SP
import requests
from sys import argv, exit
import pdfkit

class request_scrape:
	def __init__(self, url):

		self.url = url

	def get_urls(self):
		title_url = {}

		req = requests.get(self.url)
		soupy = SP(req.text)
		href = soupy.select('a')
		for h in href:
			ahref_pieces = h.get("href")
			if 'essay' in ahref_pieces and "#" not in ahref_pieces:
				href_split = ahref_pieces.split('/')[2]
				main_url = self.url.split('/bast', 1)[0]
				title_url[href_split] = "{0}{1}".format(main_url,ahref_pieces)		
		print(title_url)		
		return title_url

	def file_saver(self, url_list):


		for k, v in url_list.items():
			k_split = k.split('.')[0]

			print (k_split)

			try:
				pdfkit.from_url(v, "{}.pdf".format(k_split))
				print("[+] Converting {}".format(k_split))
			except Exception as e:
				print(str(e))

	def downloader(self, urls_dict):
		for k, v in urls_dict:
			req = requests.get(v)
			with open(k, 'w+') as temp:
				for chunk in req.iter_item(1042):
					temp.write(chunk)

		return urls_dict

	def main(self):

		one = self.get_urls()
		two = self.file_saver(one)

		print('Complete!')			


if len(argv) < 2 and len(argv) > 2:
	print('You need to use this format {} <"URL">'.format(argv[0]))
	exit(1)
else:	
	scrape = request_scrape(argv[1])
	scrape.main()


