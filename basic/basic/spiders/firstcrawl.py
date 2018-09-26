import scrapy
class urlextractor(scrapy.Spider):
	name = 'link_checker'
	with open("t1.txt", "rt") as f:
		start_urls = [url.strip() for url in f.readlines()]
	def parse(self, response):
		f = open("t1.txt",'a+')
		a_selectors = response.xpath("//a")
		for selector in a_selectors:
            # Extract the link href
			link = selector.xpath("@href").extract_first()
			if "http" in str(link):
				f.write(str(link)+'\n')
			request = response.follow(link, callback=self.parse)
#			yield request
		f.close()