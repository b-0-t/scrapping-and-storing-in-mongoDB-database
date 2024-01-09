import requests
from bs4 import BeautifulSoup

def extract_span_texts(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the HTTP response

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags with nested span tags
        anchor_tags = soup.find_all('a', {'class': 'jobtitle turnstileLink'})

        # Extract and print the text within the span tags
        for anchor_tag in anchor_tags:
            span_texts = anchor_tag.find_all('span')
            for span_text in span_texts:
                print(span_text.get_text(strip=True))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Replace 'your_url_here' with the provided Indeed job search URL
url_to_scrape = 'https://in.indeed.com/'
extract_span_texts(url_to_scrape)
