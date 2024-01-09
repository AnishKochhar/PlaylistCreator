class PrettyPrinter:

    def __init__(self, args, playlist):
        self.args = args
        self.playlist = playlist

    def displayFinalPlaylist(self):
        width = 70
        song_count = 1
        print("-" * width)
        print("Final Playlist\n".center(width))
        if "playlist" in self.playlist:
            for song in self.playlist["playlist"]:
                print("{0}. {1} - {2}".format(song_count, song[0], song[1]).center(width))
                song_count += 1
        print("-" * width)


    def printTitle(self, title):
        print('-' * (len(title) + 2))
        print(title + " |")
        print('-' * (len(title) + 2))

    def displayPlaylist(self):
        print("Here are your seeds for playlist generation: ")
        if "mood" in self.playlist:
            assert(self.args.mood != None)
            self.printTitle("Mood")
            print(self.playlist["mood"].capitalize())

        if "artist" in self.playlist:
            self.printTitle("Artist")
            print(self.playlist["artist"])

        if "year" in self.playlist:
            self.printTitle("Songs from the year")
            print(self.playlist["year"])

        if "timeframe" in self.playlist:
            assert(self.args.timeframe != None)
            monthsDict = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
                          "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
            self.printTitle("Songs from the Month of {}".format(monthsDict[str(self.args.timeframe)]))
            for song in self.playlist["timeframe"]:
                print("{0} - {1}".format(song[0], song[1]))

        if "genres" in self.playlist:
            self.printTitle("Selected Genres")
            for genre in self.playlist["genres"]:
                print(f"{genre[0]}\n- {genre[1]}")

        if "world" in self.playlist:
            self.printTitle("World Music")
            [country, decade] = self.playlist["world"]
            print("{} in the {}".format(country, decade))