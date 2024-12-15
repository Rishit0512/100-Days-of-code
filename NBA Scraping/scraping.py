import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'  # Example URL for 2024 season stats

def scrape_nba_stats(url):
    # Send a request to the website
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing player stats
    table = soup.find('table', {'id': 'per_game_stats'})
    
    # Extract table headers
    headers = [th.get_text() for th in table.find_all('thead')[0].find_all('th')]
    
    # Extract table rows
    rows = table.find('tbody').find_all('tr')
    
    data = []
    for row in rows:
        cols = row.find_all('td')
        row_data = [col.get_text() for col in cols]
        data.append(row_data)
    
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers[1:])  # Skip the first header (Rank) which is not a column

    return df

def main():
    # Scrape data
    df = scrape_nba_stats(url)
    
    # Save to CSV
    df.to_csv('nba_player_stats.csv', index=False)
    print("Data saved to nba_player_stats.csv")

if __name__ == "__main__":
    main()
