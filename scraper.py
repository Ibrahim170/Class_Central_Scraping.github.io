# scraper.py
import os
import codecs
import time
from bs4 import BeautifulSoup
from driver import get_driver

def scrape(url , dir_path):
    driver = get_driver()
    driver.get(url)
    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]

    for i, link in enumerate(links):
        if link.startswith("/"):
            link = url + link
        link = link.replace("//", "/")

        driver.get(link)
        # Wait for the translation to complete
        time.sleep(3.5)
        # Get the total height of the page
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        new_scroll_height = 200
        # Scroll down to the bottom of the page
        for j in range(0, scroll_height, 1000):
            driver.execute_script("window.scrollTo(0, " + str(j) + ")")
            time.sleep(1)  # Pause for 1 second between each scroll
        # Obtain page source
        h = driver.page_source

        path = f"{dir_path}/Page{i}.html"
        # Open file in write mode with encoding
        file = codecs.open(path, "w", "utf-8")

        # Write page source content to file
        file.write(h)

    # Close the browser
    driver.quit()