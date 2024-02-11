from bs4 import BeautifulSoup
import requests

# Get songList from specified Rolling Stones
def scrape_song_lyrics(url):
    page = BeautifulSoup(requests.get(url).content, 'lxml')
    with open("song_list.txt", "w") as songList:
        for tag in page.select('h2', {'class':'c-gallery-vertical-album__title'}):
            line = tag.get_text(strip=True, separator='\n')
            if line:
                print(line)
                songList.write(line + '\n')

    return True

scrape_song_lyrics("https://www.rollingstone.com/music/music-lists/500-greatest-songs-of-all-time-151127")