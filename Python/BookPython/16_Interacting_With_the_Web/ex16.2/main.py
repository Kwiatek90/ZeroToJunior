#1. Write a script that grabs the full HTML from the page
#http://olympus.realpython.org/profiles
#2. Parse out a list of all the links on the page using Beautiful Soup by
#looking for HTML tags with the name a and retrieving the value
#taken on by the href attribute of each tag.
#3. Get the HTML from each of the pages in the list by adding the full
#path to the file name, and display the text (without HTML tags) on
#each page using Beautiful Soup’s .get_text() method.

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"

page =urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

for anchor in soup.find_all("a"):
    link_address = url + anchor['href']
    print(anchor)
    print(link_address)
    
    
