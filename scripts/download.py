import subprocess
''' 
Improvements:
    Environment variable for path to local Music folder
'''

class Download(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("Creating new Download instance")
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    # 1. Gets the song's YouTube URL
    # 2. Runs yt-dlp process to download the URL as an mp3 file locally
    @classmethod
    def download(cls, songname, artist, baseFilepath="Music"):
        print(f"-- Beginning download of {songname}")

        id = cls.findSong(songname, artist)
        filepath = f"{baseFilepath}/{songname}.mp3"
        url = f"https://www.youtube.com/watch?v={id}"
        subprocess.run(['yt-dlp', '-xci', '--audio-quality', '0', '--audio-format', 'mp3', '-o', filepath, url])
        
        print(f"-- {songname} has been downloaded to {filepath}")

    # 1. Finds the URL that best matches the songname and artist given on YouTube
    @classmethod
    def findSong(cls, songname, artist):
        search_query = f"ytsearch:{songname} - {artist}"

        result = subprocess.run(['yt-dlp', search_query, '--get-id'],
                                capture_output = True, 
                                text = True)
        id = result.stdout.strip('\n')
        print(f"-- Song ID: {id}")
        return id if id != "" else "pT68FS3YbQ4" # Return You Only Live Once if nothing retured