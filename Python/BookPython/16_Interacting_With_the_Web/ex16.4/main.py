#1. Use Mechanical Soup to provide the correct username “zeus” and
#password “ThunderDude” to the login page submission form located at http://olympus.realpython.org/login.

#2. Display the title of the current page to determine that you have
#been redirected to the /profiles page.

#3. Use Mechanical Soup to return to login page by going “back” to the
#previous page.

#4. Provide an incorrect username and password to the login form,
#then search the HTML of the returned webpage for the text
#“Wrong username or password!” to determine that the login
#process failed.
#1
import mechanicalsoup

browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

#2
title = profiles_page.soup.select("title")
title = title[0].text
print(title)

#3
login_page = browser.get(url)
login_title = login_page.soup.title
print(f"Title: {login_title.text}")

#4
login_html = login_page.soup
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDudee"

profiles_page = browser.submit(form, login_page.url)

if profiles_page.soup.text.find("Wrong username or password!"):
    print("Wrong username or password!")
else:
    pass