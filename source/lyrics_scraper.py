import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re

# Get the Genius API key from the environment variable
load_dotenv("source\GENIUS_API_KEY.env")
genius_api_key = os.getenv("GENIUS_API_KEY")

# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + genius_api_key}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response

# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)
    
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
            
        if (len(songs) == song_cap):
            break
        else:
            page += 1
        
    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs
    
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

# Get first 10 results from Frank Sinatra and return lyrics to the first
scrape_song_lyrics(request_song_url('Frank Sinatra', 10)[0])
