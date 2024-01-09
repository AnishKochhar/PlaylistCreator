import sys, argparse
import download as Downloader, uploader as Uploader, generator as Generator

def parse():
    parser = argparse.ArgumentParser(prog="Playlist Composer")
    parser.add_argument("-g", "--genre", type=int, choices=range(2, 6), default=3)
    parser.add_argument("-t", "--timeframe", type=int, choices=range(1, 13))
    parser.add_argument("-w", "--world", action="store_true")
    parser.add_argument("-a", "--artist")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-y", "--year", type=int, choices=range(1800, 2024), 
                        help="Specify a particular year song selection, ensuring songs from that specific year are included")
    parser.add_argument("-l", "--limit", type=int, default=30)
    parser.add_argument("-m", "--mood", type=str)
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("-i", "--interactive", action="store_true")
    args = parser.parse_args()
    return args

def generate(args):
    generator = Generator.Generator(args)
    playlist = generator.generate()
    return playlist

def upload(playlist):
    user_input = input("Would you like to upload this playlist to Spotify? Press enter to accept ")
    if user_input == "":
        uploader = Uploader.SpotifyUploader()
        uploader.upload(playlist)
    user_input = input("Would you like to download the playlist locally? Press enter to accept ")
    if user_input == "":
        downloader = Downloader.Download.instance()
        for songname, artist in playlist:
            downloader.download(songname, artist)

if __name__ == "__main__":
    args = parse()
    playlist = generate(args)
    upload(playlist)
    print("Terminating playlist creator!")
