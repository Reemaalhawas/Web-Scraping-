import requests

# The URL for the IMDB Top 250 Movies
url = 'https://www.imdb.com/chart/top/'

# Define headers to mimic a web browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send the HTTP GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Page successfully retrieved!")
    # You can print the content or parse the HTML here
    print(response.content)  # This will print the raw HTML of the page
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
