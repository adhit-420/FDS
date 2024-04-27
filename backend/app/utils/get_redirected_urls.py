import requests
from bs4 import BeautifulSoup
import urllib.parse


def get_redirected_urls(url):
    try:
        response = requests.get(url, allow_redirects=True000000000000)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.find_all("a", href=True)
            redirected_urls = []
            for link in links:
                href = link["href"]
                full_url = urllib.parse.urljoin(url, href)
                redirected_url = requests.head(full_url, allow_redirects=True).url
                if redirected_url != full_url:
                    redirected_urls.append((full_url, redirected_url))
            return redirected_urls
        else:
            print("Failed to fetch URL:", url)
            return []
    except Exception as e:
        print("An error occurred:", str(e))
        return []
