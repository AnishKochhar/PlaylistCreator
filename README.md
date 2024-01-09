A terminal application that creates personalised playlists based on a wide range of command line arguments.

Can be used to **generate** playlists (and store them locally in text files), **download** playlists (finding songs on YouTube and downloading mp3's locally), and **upload** the playlist to your personal Spotify account for easy listening.

Uses OpenAI's ChatGPT chatbot to give song recommendations based on music taste

## Examples

#### Example 1

##### Note: As explained in the Usage section, you first receive a *seed* of your playlist from which the final playlist is built. You may re-seed as many times are you like.

Let's create a  a playlist using 3 seed genres: `-g 3`;  including 5 songs I listened to in October: `-t 10`;  picking songs from artists similar to *King Krule*: `--artist="King Krule"`; and 5 random songs from the year 1999: `-y 1999`. The program should then save the playlist to the file *sample_playlist.txt* `-o "playlists/sample_playlist.txt"` 

Prompt the program with 
```
python3 scripts/main.py -g 3 -t 10 --artist="King Krule" -y 1999 -o "playlists/sample_playlist.txt" 
```

<img src="demo/Demo%201%20-%20Prompt.png" alt="Save to file prompt" >
<img src="demo/Demo%201%20-%20Playlist%20Creation.png" alt="Save to file result" >

Look inside playlists/sample_playlist.txt to see the result of this command

#### Example 2
Let's say you wanted to generate a different playlist in a 'chill' mood, then add some specific songs you like, and have it uploaded to your Spotify account. 

In this playlist there will be 4 seed genres: `--genre=4`;  some world music will be included: `--world`;  using "Nujabes" as the seed artist: `--artist="Nujabes`;  the mood with be "chill: `--mood="chill"`; and it should be interactive: `-i`.

Prompt the program with 
```
python3 scripts/main.py --genre=3 --world --artist="Nujabes" --mood="chill" -i
```

<img src="demo/Demo%202%20-%20Prompt.png" alt="Interactive prompt" >
<img src="demo/Demo%202%20-%20Playlist%20Creation.png" alt="Interactive prompt">

Here I can add arbitrary songs (e.g. *One More Time by Daft Punk*), and remove songs from the given playlist (e.g. *The Scientist by Coldplay*)

<img src="demo/Demo%202%20-%20Uploading.png" alt="Interactive prompt" >

This playlist has now been uploaded to your Spotify page with the playlist name of today's current date
<img src="demo/Demo%202%20-%20Spotify.png" alt="Interactive prompt" >

You can also tell the program: to be *verbose*, i.e. show raw results from Spotify and OpenAI APIs. Also, you can *limit* the number of songs in the final playlist.

Depending on your instructions when running, you can download the entire playlist locally as well. You can change the storage folder (e.g. to your local machines Desktop) inside `download.py`

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


*See example screenshots for arguments guide*


### Dependencies
This repository is built using the following Python libraries (*pip install*)
- [openai](https://platform.openai.com/docs/overview): for interacting with the OpenAI api
- [spotipy](https://github.com/spotipy-dev/spotipy): for uploading the playlist to Spotify
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): for downloading songs from YouTube


Enjoy your new playlists!