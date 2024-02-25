import requests
from bs4 import BeautifulSoup
from downloader import downloadFile
import concurrent.futures

def process_data(item):
    seasonName="Season 7-Advanced Challenge"
    Name= item['name']
    URL= item['url']
    downloadFile(Name,seasonName,URL)

def extract_links(url):
    finalURL=[]
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor (a) tags in the HTML
            links = soup.find_all('a')

            # Extract and print the href attribute from each link
            for link in links:
                href = link.get('href')
                if href and  href.endswith('.mp4'):
                    text = link.get_text(strip=True)
                    if text.endswith("download"):
                        text = text[:-8]  # Remove the last 8 characters ("download")
                    finalURL+=[{"name":text,"url":href}]

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")
    return finalURL




url=extract_links('https://archive.org/details/pokemon-advanced-challenge-the-complete-collection-4kids-entertainment-english-dub')
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_data, url)