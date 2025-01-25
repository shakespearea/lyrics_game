import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re
from fuzzywuzzy import fuzz

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
            #print('No songs found with the title "{}" by {}'.format(song_title, artist_name))
            return None

        # Song must match the song title and artist
        for hit in json['response']['hits']:
            if (fuzz.partial_ratio(song_title.lower(), hit['result']['title'].lower()) > 70 and
                    fuzz.partial_ratio(artist_name.lower(), hit['result']['primary_artist']['name'].lower()) > 70):
                return hit['result']['url']

# Get lyrics from specified Genius.com song URL
def scrape_song_lyrics(url):
    page = BeautifulSoup(requests.get(url).content, 'lxml')
    with open("lyrics.txt", "w", encoding='ascii', errors='ignore') as lyrics:
        for tag in page.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
            line = tag.get_text(strip=True, separator='\n')
            if line:
                print(line)
                lyrics.write(line)

    return True

success = 0
failure = 0

# Read and process only the first 250 songs
with open('song_list.txt', 'r', encoding='utf-8') as file:
    song_list = [line.strip() for line in file.readlines()][:250]

for song in song_list:
    # Split the string by the last comma only
    parts = song.rsplit(", ‘", 1)
    if len(parts) == 2:
        artist, title = parts
        # Remove the ending quote if it exists
        if title.endswith('’'):
            title = title[:-1]

        # Call your function with the unmodified artist and title
        song_url = request_song_url(title, artist, 5)

        if song_url == None:
            failure += 1
            print(f'Failed: "{title}" by {artist}')
        else:
            success += 1
    else:
        failure += 1
        print(f"Error processing song details: {parts}")

print(f"Processing complete. {failure} failed songs out of {failure + success}")