import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Get the Genius API key from the environment variable
load_dotenv("source\GENIUS_API_KEY.env")
genius_api_key = os.getenv("GENIUS_API_KEY")

# Get song object from Genius API
def request_song_info(song_title, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + genius_api_key}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': song_title}
    response = requests.get(search_url, data=data, headers=headers)
    return response

def request_song_url(song_title, artist_name, page_cap):
    for i in range(1, page_cap):
        page = i

        response = request_song_info(song_title, page)
        json = response.json()

        # Exit if no results found
        if not json['response']['hits']:
            print('No songs found with the title "{}" by {}'.format(song_title, artist_name))
            return None

        # Song must match the song title and artist
        for hit in json['response']['hits']:
            if (song_title.lower() in hit['result']['title'].lower() and
                    artist_name.lower() in hit['result']['primary_artist']['name'].lower()):
                return hit['result']['url']

    print('No songs found with the title "{}" by {}'.format(song_title, artist_name))

# Get lyrics from specified Genius.com song URL
def scrape_song_lyrics(url):
    page = BeautifulSoup(requests.get(url).content, 'lxml')
    with open("lyrics.txt", "w") as lyrics:
        for tag in page.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
            line = tag.get_text(strip=True, separator='\n')
            if line:
                print(line)
                lyrics.write(line)

    return True

# Search lyrics for 'Fly me to the Moon' by Frank Sinatra within 5 pages of search results.
song_url = request_song_url('Fly me to the Moon', 'Frank Sinatra', 5)
if song_url:
    scrape_song_lyrics(song_url)