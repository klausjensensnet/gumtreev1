import scraperwiki

# Blank Python

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

webpage = urlopen('http://www.gumtree.com/search?q=boxster&search_category=porsche').read()

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

