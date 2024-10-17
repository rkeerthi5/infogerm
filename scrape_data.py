import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'lxml')

            # Extract specific data (e.g., headlines)
            # Example for CNN - headlines are inside <h3> tags with class 'cd__headline-text'
            headlines = soup.find_all('h3', class_='cd__headline-text')

            # Handle missing data (if the website structure changes)
            if not headlines:
                print("No headlines found. The website structure might have changed.")
                return

            # Display the headlines in the terminal
            print("News Headlines:")
            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline.text.strip()}")

        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # URL of the website to scrape
    url = "https://www.cnn.com/world"
    
    # Call the scraping function
    scrape_website(url)
