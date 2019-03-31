from bs4 import BeautifulSoup as bs
import requests, os



def linkExtract():

	url = 'https://xkcd.com'
	while not url.endswith('#'):
		req = requests.get(url)
		soup = bs(req.text, "lxml")
		src = soup.select('img[srcset]')
		if src == []:
			pass
		else:	
			fulllink = 'http:'+ src[0].get('src')
			print(fulllink)
			with open('xkcd/xkcd.txt', 'a') as xkcd:
				xkcd.write(fulllink + ',')

		prev = soup.select('li > a[accesskey="p"]')
		if prev:
			url = 'https://xkcd.com' + prev[0].get('href')	
			continue
			

def imgWrite():
	with open('xkcd/xkcd.txt', 'r') as xkcd:
		data = xkcd.read()

	imgSrc = data.split(',')
	try:
		for img in imgSrc:
			req = requests.get(img)
			name = img.split('/')
			with open('/home/seachel/Python/spiders/scrapy-tutorials/xkcd/'+name[4], 'wb') as pic:
				for chunk in req.iter_content(1024):
					pic.write(chunk)
	except requests.exceptions.MissingSchema:
		pass

if not os.path.isdir('xkcd/'):
	os.mkdir('xkcd')

linkExtract()
imgWrite()