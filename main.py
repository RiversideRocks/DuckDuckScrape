import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import time
import random
import os

def download_pdf(url, folder):
    response = requests.get(url)
    filename = os.path.basename(url)

    with open(os.path.join(folder, filename), 'wb') as file:
        file.write(response.content)

    print(f"{filename} saved to {folder}")

# "site:justice.gov filetype:pdf \"v.\""
def scraper(q, p, d):
    WAIT_LOW = 5
    WAIT_HIGH = 15
    PAGES = p

    # Set the base URL for the search and the query parameters
    base_url = "https://duckduckgo.com/html/"
    params = {"q": q, "s": "0"}

    # Create an empty list to store the links
    links = []

    print("Preparing to scrape DuckDuckGo.")
    print("================================")
    print("Estimated time: " + str((WAIT_LOW * PAGES)) + "s - " + str((WAIT_HIGH * PAGES)) + "s")
    print("Time per link: " + str((PAGES * 30) / (((WAIT_LOW + WAIT_HIGH) / 2) * PAGES)) + "urls/s (avg)")

    # Loop through the first 10 pages of the search results
    for i in range(PAGES):
        # Update the start index parameter for each page
        params["s"] = str(i * 10)

        # Send a GET request to the search URL with the query parameters
        response = requests.get(base_url, params=params, headers={"User-agent": "dssdfsfuh3f982hf9h32f8h823hfdsfhsjkfhsdjfhkhsdfjh"})

        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the <a> tags with class "result__url" and extract the href attribute
        for link in soup.find_all("a", class_="result__url"):
            parsed_url = urlparse(link["href"])
            query_dict = parse_qs(parsed_url.query)
            print("HIT for " + query_dict['uddg'][0])
            r = requests.get(query_dict['uddg'][0], headers={"User-agent": "archive"})
            size = round(int(r.headers["content-length"])/1024, 3)
            print("Size: " + str(size) + "KB")
            download_pdf(query_dict['uddg'][0], d)
            links.append(query_dict['uddg'][0])
        time.sleep(random.randint(5,15))

    # Print the list of links
    print(links)
    print("Scraped " + str(len(links)) + " from DuckDuckGo")