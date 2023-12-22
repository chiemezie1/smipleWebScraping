# Importing all the necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Opening the link using Webdriver
link = "https://quotes.toscrape.com/"
driver = webdriver.Chrome()
driver.get((link))
raw_html = urlopen(link)
first_page = BeautifulSoup(raw_html, "html.parser")

# Navigating to the next page by clicking next
login_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
login_button.click()

# Get the link of the current page and opening
current_page_url = driver.current_url

# Taking raw web content in bytes format and converting it into a readable string format using the UTF-8 encoding
page = urlopen(current_page_url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Use beautifulSoup package to parse and read them
soup = BeautifulSoup(html, "html.parser")
text = soup.find_all("span", class_="text")

# Print out each quote
for obj in text:
    print(obj.get_text())
