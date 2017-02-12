#proj2.py
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
url = 'http://nytimes.com'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
story_headline = soup.find_all('h2',{"class":'story-heading'})
for heading in story_headline[:10]:
	if heading.a:
		print(heading.a.get_text().replace("\n"," ").strip())
	else:
		print(heading.contents[0].strip())


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
url2 = 'https://www.michigandaily.com/'
html = urlopen(url2, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
most_read = soup.find('div',{'class':'view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266'})
li_most_read = most_read.div.ol
li_tags = li_most_read.find_all('li')
for l in li_tags:
	if l.a:
		print(l.a.get_text().replace("\n"," ").strip())
	else:
		print(l.contents[0].strip())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
url3 = 'http://newmantaylor.com/gallery.html'
html = urlopen(url3, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
img_tags = soup.find_all('img')
for img in img_tags:
	if img.get('alt'):
		print (img['alt'])
	else:
		print ("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
baseurl = 'https://www.si.umich.edu'
url4 = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
html = urlopen(url4, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
next_page = soup.find('a',{'title':'Go to next page'})
alt_tags = [] 
content = soup.find('div', {'class':'view-content'})
a_tags = content.find_all('a')
for a in a_tags:
	if a.get_text() == 'Contact Details':
		alt_tags.append(a.get('href'))

while next_page:
	next_page = soup.find('a',{'title':'Go to next page'})
	try:
		url4 = baseurl + next_page.get('href')
		html = urlopen(url4, context=ctx).read()
		soup = BeautifulSoup(html, "html.parser")
		content = soup.find('div', {'class':'view-content'})
		a_tags = content.find_all('a')
		for a in a_tags:
			if a.get_text() == 'Contact Details':
				alt_tags.append(a.get('href'))
	except:
		next_page = False

	# next_page = soup.find('a', {'title':'Go to next page'})

for i in range(len(alt_tags)):
	url5 = baseurl + alt_tags[i]
	html5 = urlopen(url5, context=ctx).read()
	soup = BeautifulSoup(html5, "html.parser")
	content5 = soup.find('div', {'class':'column panel'})
	print (str(i + 1) + ' ' + content5.a.get_text())








