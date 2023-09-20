#1.Write a script that grabs the full HTML from the page
#http://olympus.realpython.org/profiles/dionysus

#2. Use the string .find() method to display the text following “Name:”
#and “Favorite Color:” (not including any leading spaces or trailing
#HTML tags that might appear on the same line).

#3. Repeat the previous exercise using regular expressions. The end
#of each pattern should be a “<” (the start of an HTML tag) or a newline character, and you should remove any extra spaces or newline
#characters from the resulting text using the string .strip() method.

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

#<h2>Name: Dionysus</h2>
start_tag = "<h2>"
end_tag = "</h2>"
start_index = html.find(start_tag) + len(start_tag)
end_index = html.find(end_tag)

#<br>Favorite Color: Wine</center>
start_tag_2 = "<br>"
end_tag_2 = "</center>"
start_index_2 = html.find(start_tag_2) + len(start_tag_2)
end_index_2 = html.find(end_tag_2)

print(html[start_index_2:end_index_2])

#<h2>Name: Dionysus</h2>
pattern = "<h2.*?>.*?</h2.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tag
print(title)

#<br>Favorite Color: Wine</center> # blad
pattern_2 = "<br>Favorite Color: Wine</center>"
match_results_2 = re.search(pattern_2, html, re.IGNORECASE)
title_2 = match_results_2.group()
title_2 = re.sub("<.*?>", "", title_2) # Remove HTML tag
print(title_2)