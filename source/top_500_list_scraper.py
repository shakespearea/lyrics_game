from bs4 import BeautifulSoup
import requests

# Create text file containing Rolling Stones top 500
def scrape_song_lyrics(url_list):
    line_count = 0
    with open("song_list.txt", "w", encoding="utf-8") as song_list:
        for url in url_list:
            page = BeautifulSoup(requests.get(url).content, 'lxml')
            for tag in page.select('h2', {'class':'c-gallery-vertical-album__title'}):
                line = tag.get_text(strip=True, separator='\n')
                if line and line not in ["The Latest", "Most Popular", "You might also like"]:
                    print(line)
                    song_list.write(line + '\n')
                    line_count+=1
    print(f"\n{line_count} song titles found and written to song_list.txt")
    return True

# As the webpage for the Rolling Stones is dynamically generated, 
# the most straight-forward solution to getting the full list was to request each page indiviually.
# Each url corresponds to 50 songs: 500-451, 450 - 401, etc.
rs_top_500_2021 = ["https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/kanye-west-stronger-1224837/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/neil-young-powderfinger-1224887/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/david-bowie-station-to-station-3-1224938/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/john-prine-angel-from-montgomery-1224988/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/the-b-52s-rock-lobster-2-1225038/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/jimi-hendrix-purple-haze-2-1225088/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/david-bowie-changes-2-1225138/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/green-day-basket-case-1225188/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/bob-dylan-blowin-in-the-wind-3-1225238/",
                   "https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/daddy-yankee-feat-glory-gasolina-1225288/"]
scrape_song_lyrics(rs_top_500_2021)