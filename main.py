import sys, argparse
import download, uploader as Uploader, generator as Generator

def parse():
    parser = argparse.ArgumentParser(prog="Playlist Composer")
    parser.add_argument("-g", "--genre", type=int, choices=range(2, 6), default=3)
    parser.add_argument("-t", "--timeframe", type=int, choices=range(1, 13))
    parser.add_argument("-w", "--world", action="store_true")
    parser.add_argument("-a", "--artist")
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
        print("TODO: downloading")

if __name__ == "__main__":
    args = parse()
    playlist = generate(args)
    upload(playlist)
    print("Terminating playlist creator!")
