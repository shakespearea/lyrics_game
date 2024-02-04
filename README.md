# Lyrics Quiz Game

## Aim
This repo is dedicated to the development of a game that gets players to guess statistics-based questions of popular games.

Lyrics of popular songs are to be scraped from the internet and then these will be analysed and used to generate quiz questions.

Example Questions: 
  - How many times does the word "imagine" appear in the song 'Imagine' by John Lennon?
  - Is the word "love" mentioned more times in the song 'Crazy Little Thing Called Love' by Queen or in 'What is Love' by Haddaway?

## Build Instructions
1. Clone the repository (or download)
```bash
git clone https://github.com/shakespearea/lyrics_game.git
```
2. Install the required modules
```bash
pip install requests beautifulsoup4
pip install lxml
pip install python-dotenv
```
3. Generate a (free) API key for Genius at:
   http://genius.com/api-clients
4. Paste the "Client access token" into [`GENIUS_API_KEY.env`](./source/GENIUS_API_KEY.env):
```
GENIUS_API_KEY=paste-your-api-key-here
```

---
DISCLAIMER:
This project is an educational exercise and proof of concept for web scraping using Python. The purpose of this project is to demonstrate the process of accessing and extracting publicly available information from a specific website that provides lyrics.

Usage Considerations:
1. **Expletives and Content: This tool may extract lyrics that include expletives or mature content. As the game developer, you are responsible for filtering and presenting statistics in a manner consistent with the intended audience of your game.
2. Ownership Disclaimer: The lyrics retrieved by this tool are not owned by the developer. They remain the property of their respective copyright holders. The lyrics obtained from this tool are utilised solely for generating statistics within the context of the game. Users will see statistical insights derived from the lyrics rather than the lyrics themselves.

By using this project, you acknowledge that the lyrics remain the property of their respective copyright holders and agree to abide by the terms of the MIT License.
