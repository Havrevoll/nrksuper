import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_links(soup):
    # Placeholder for link extraction logic
    # You can customize this function to extract the specific links you need
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    return links

def main():
    url = 'http://example.com'  # Replace with the actual URL
    html_content = fetch_website_content(url)
    if html_content:
        soup = parse_html(html_content)
        links = extract_links(soup)
        for link in links:
            print(link)

if __name__ == '__main__':
    main()
