import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        pass

    def get_plain_text(self, url):
        # Send a GET request to the URL
        response = requests.get(url)

        # Create a BeautifulSoup object with the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup.get_text()
