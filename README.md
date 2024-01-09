A terminal application that creates personalised playlists based on a wide range of command line arguments.

Can be used to **generate** playlists (and store them locally in text files), **download** playlists (finding songs on YouTube and downloading mp3's locally), and **upload** the playlist to your personal Spotify account for easy listening.

Uses OpenAI's ChatGPT chatbot to give song recommendations based on music taste

## Examples

#### Example screenshots to be added

## Installation

**Step 1:** Create an [OpenAI account](https://beta.openai.com/account/api-keys)

**Step 2:** Generate [Spotify Client ID & Secret Key](https://developer.spotify.com/dashboard/login) and set a Redirect URI under your App settings, e.g. `http://localhost:3000`.

**Step 3:** Install dependencies (recommended inside of virtual environment)

```
pip install spotipy
```
**Step 4:** Setup credentials

This can be done via executing the following commands in Terminal OR creating a *.env* file in the root directory.
```
export OPENAI_API_KEY="OpenAI API key"
export SPOTIPY_CLIENT_ID="Spotify Client ID"
export SPOTIPY_CLIENT_SECRET="Spotify Client Secret"
export SPOTIPY_REDIRECT_URI="Redirect URI, e.g. http://localhost:3000"
```


## Usage

Activate the virtual environment and run the main script by
```
source .venv/bin/activate
python3 scripts/main.py <arguments>
```
You will be prompted with a seed for the playlist (all the inputs that will be given to ChatGPT as prompts for more songs). You may request a re-seed as many times as you choose.

You will then be presented with the final playlist. If *--interactive* is set you can then modify the playlist to remove/include any songs.

You can then choose to upload the playlist to your Spotify account.

Finally, you can choose to download the playlist in *.mp3* format to your machine.

### Arguments:

| Short | Long | Description |
| ----------- | -- | ----------- |
| *-g \<n>* | *--genre=\<n>* | Pick *n* genres from Models/genres.txt. You can edit this file to contain your genres. *Defaults to 3* |
|*-t \<n>* | *--timeframe=\<n>* | Picks 5 songs from the *n*'th month of listening history stored in Models/listening_history.json |
|*-a \<name>* | *--artist=\<name>* | Find songs from artists similar to *name* |
| *-w* | *--world*| Use a random country and decade in the playlist |
|*-v* | *--verbose* | Provides more details about the playlist generation process |
|*-y \<year>* | *--year \<year>* | Specify a particular year song selection, ensuring songs from that specific year are included |
| *-l \<n>* | *--limit \<n>*| Specify the maximum number of songs in the playlist. *Defaults to 30* |
| *-m \<mood>* | *--mood \<mood>* | Input mood paramter (e.g. happy, sad, energetic) to influence prompting |
| *-i* | *--interactive* | Allow interactive refining and modification of playlist after final generation |
| *-o \<filepath>* | *--output \<filepath>*| Save the generated playlist to specified output file |


**See example screenshots for examples of arguments' effects**


### Dependencies
This repository is built using the following Python libraries (*pip install*)
- [openai](https://platform.openai.com/docs/overview): for interacting with the OpenAI api
- [spotipy](https://github.com/spotipy-dev/spotipy): for uploading the playlist to Spotify
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): for downloading songs from YouTube


Enjoy your new playlists!