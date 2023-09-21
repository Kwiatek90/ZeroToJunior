import time
import mechanicalsoup
browser = mechanicalsoup.Browser()
for i in range(5):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    tag_time = page.soup.select("#time")[0]
    result_time = tag_time.text
    result = tag.text
    print(f"The result of your dice roll is: {result} on {result_time}")
# Wait 30 seconds if this isn't the last request
    if i < 3:
        time.sleep(1)
