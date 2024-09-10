import requests
from bs4 import BeautifulSoup

# Define headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a request to the website
response = requests.get('https://sa.aqar.fm/', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful")

    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the title of the page
    print("Page Title: ", soup.title.string)

    # Example: Find and print all links on the page
    for link in soup.find_all('a'):
        print(link.get('href'))

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
