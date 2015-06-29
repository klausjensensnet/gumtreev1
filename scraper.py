import scraperwiki

# Blank Python

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

webpage = urlopen('http://www.gumtree.com/search?q=boxster&tq=%7B%22i%22%3A%22boxster%22%2C%22s%22%3A%22boxster%22%2C%22p%22%3A0%2C%22t%22%3A13%7D&search_category=porsche&search_location=&distance=0.0001').read()

soup = BeautifulSoup(webpage)
# get the link to the profile page
soup.findAll(attr={"<a href=" : "class="})
print soup.findAll(attr={"<a href=" : "class="})

# get short description
soup.findAll(attr={"</a><br/>" : "</td>"})
print soup.findAll(attr={"</a><br/>" : "</td>"})

# get time posted
soup.findAll(attr={"<td class="'posted'">" : "<ul>"})
print soup.findAll(attr={"<td class="'posted'">" : "ul>"})

# get location
soup.findAll(attr={"<li>" : "<ul>"})
print soup.findAll(attr={"<li>" : "</li>"})

# get Headline
soup.findAll(attr={"class="'adLinkSB'">" : "</a><br/>"})
print soup.findAll(attr={"class="'adLinkSB'">" : "</a><br/>"})


# OLD CODE:
# soup.findAll(attr={"class" : "resultsTableSB"})

# print soup.findAll(attr={"class" : "resultsTableSB"}) 

