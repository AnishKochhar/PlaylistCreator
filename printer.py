class PrettyPrinter:

    def __init__(self, args, playlist):
        self.args = args
        self.playlist = playlist

    def displayFinalPlaylist(self):
        width = 70
        song_count = 1
        print("-" * width)
        print("Final Playlist\n".center(width))
        if "timeframe" in self.playlist:
            for song in self.playlist["timeframe"]:
                print("{0}. {1} - {2}".format(song_count, song[0], song[1]).center(width))
                song_count += 1
        if "genres" in self.playlist:
            for song in self.playlist["genres"]:
                print("{0}. {1} - {2}".format(song_count, song[0], song[1]).center(width))
                song_count += 1
        if "artist" in self.playlist:
            for song in self.playlist["artist"]:
                print("{0}. {1} - {2}".format(song_count, song[0], song[1]).center(width))
                song_count += 1
        if "world" in self.playlist:
            for song in self.playlist["world"]:
                print("{0}. {1} - {2}".format(song_count, song[0], song[1]).center(width))
                song_count += 1
        print("-" * width)


    def printTitle(self, title):
        print('-' * (len(title) + 2))
        print(title + " |")
        print('-' * (len(title) + 2))

    def displayPlaylist(self):
        print("PLAYLIST SEEDS: ")
        if "timeframe" in self.playlist:
            assert(self.args.timeframe != None)
            monthsDict = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
                          "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
            self.printTitle("Songs from the Month of {}".format(monthsDict[str(self.args.timeframe)]))
            for song in self.playlist["timeframe"]:
                print("{0} - {1}".format(song[0], song[1]))
        if "genres" in self.playlist:
            assert(self.args.genre != None)
            self.printTitle("Selected Genres")
            for genre in self.playlist["genres"]:
                print(f"{genre[0]}\n- {genre[1]}")
        if "world" in self.playlist:
            self.printTitle("World Music")
            [country, decade] = self.playlist["world"]
            print("{} in the {}".format(country, decade))
        if "artist" in self.playlist:
            self.printTitle("Artist")
            print(self.playlist["artist"])