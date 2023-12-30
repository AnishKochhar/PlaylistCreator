A terminal application that creates playlists based on a. listening history, b. genre choices, c. random world music, and d. a given artist.

Uses ChatGPT to give song recommendations

## Examples

#### Example screenshots to be added

## Usage Instructions

Activate the virtual environment by running `source .venv/bin/activate`

`python3 scripts/main.py <arguments>`

### Arguments:

<!-- - *-w*: Use a random country and decade in the playlist
- *-g \<n>*: Use *n* genres from Models/genres.txt. *Defaults to 3.*
- *-t \<n>*: Picks 5 songs from the *n*'th month of my listening history -->

| Short | Long | Description |
| ----------- | -- | ----------- |
| *-w* | *--world*| Use a random country and decade in the playlist |
| *-g \<n>* | *--genre=\<n>* | Pick *n* genres from Models/genres.txt. *Defaults to 3.* |
|*-t \<n>* | *--timeframe=\<n>* | Picks 5 songs from the *n*'th month of listening history |
|*-a \<name>* | *--artist=\<name>* | Find songs from artists similar to *name* |

### Dependencies
- openai: for interacting with the OpenAI api
- spotipy: for uploading the playlist to Spotify
- yt-dlp: for downloading songs from YouTube
## Setup
You must setup the following environment variables:
1. OPENAI_API_KEY: https://platform.openai.com/api-keys
2. SPOTIPY_CLIENT_ID
3. SPOTIPY_CLIENT_SECRET
4. SPOTIPY_REDIRECT_URI