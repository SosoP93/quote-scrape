import requests
from bs4 import BeautifulSoup
from csv import reader, writer



def soup_request(url):
	""" Get html of website and turn into BeautifulSoup object
	so that we can navigate html for information"""
	r = requests.get(url)
	
	soup = BeautifulSoup(r.text, "html.parser")
	return soup

	

def scraper(soup):
	""" scrape information from html and add into a list"""

	# target 'class = quote' in order to gather quote content
	quotes = soup.select(".quote")

	# empty list for adding in the lists of quotes
	info = []

	for quote in quotes:
		content = quote.select(".text")[0].get_text()
		author_name = quote.select(".author")[0].get_text()
		author_ref = quote.select("a")[0]["href"]
		about_author = soup_request(url + author_ref)
		author_born = about_author.select(".author-born-date")[0].get_text()
		author_bplace = about_author.select(".author-born-location")[0].get_text()
		info.append([author_name, content, author_born, author_bplace])
	return info



def write_csv(contents):
	""" Create new file and write content in it"""
	with open("quotes.csv", "w", encoding = "utf-8") as csv_file:
		csv_write = writer(csv_file)

		for content in contents:
			csv_write.writerow(content)



def append_csv(contents):
	""" Open existing file and add content to it"""
	with open("quotes.csv", "a", encoding = "utf-8") as csv_file:
		csv_append = writer(csv_file)

		for content in contents:
			csv_append.writerow(content)



# url that will be scraped
url = "http://quotes.toscrape.com"
main_page = soup_request(url)
contents = scraper(main_page)
write_csv(contents)


# While a class called 'next' exists in the html, this loop will
# scrape the page, append rows to the csv file, and then
# move to next page
page_num = 1

test = True
while test:
	page_num += 1	
	next_page_url = url + f"/page/{page_num}"
	next_page = soup_request(next_page_url)
	info = scraper(next_page)
	append_csv(info)

	if not next_page.select(".next"):
		test = False


	



