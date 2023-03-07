import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# Set the base URL for the search and the query parameters
base_url = "https://duckduckgo.com/html/"
params = {"q": "site:justice.gov filetype:pdf", "s": "0"}

# Create an empty list to store the links
links = []

# Loop through the first 10 pages of the search results
for i in range(10):
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
        links.append(query_dict['uddg'][0])

# Print the list of links
print(links)
