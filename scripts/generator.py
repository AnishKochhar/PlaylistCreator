import json, random, os
from prompter import Prompter
from printer import PrettyPrinter

class Generator:

    def __init__(self, args):
        self.args = args
        self.playlist = {}

    def printExtendedPlaylist(self):
        prettyPrinter = PrettyPrinter(self.args, self.playlist)
        prettyPrinter.displayPlaylist()

    def printPlaylist(self):
        prettyPrinter = PrettyPrinter(self.args, self.playlist)
        prettyPrinter.displayFinalPlaylist()

    def savePlaylist(self, filepath):
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory) or not os.access(directory, os.W_OK):
            print(f"Error: Directory '{directory}' does not exist or is not writable.")
            return

        if os.path.exists(filepath) and not os.access(filepath, os.W_OK):
            print(f"Error: File '{filepath}' is not writable.")
            return 
        
        with open(filepath, "w") as output_file:
            song_count = 0
            if "playlist" in self.playlist:
                for song in self.playlist["playlist"]:
                    output_file.write("{}. {} - {}\n".format(song_count, song[0], song[1]))
                    song_count += 1
            print(f"Playlist successfully written to {filepath}")

    def interactivePlaylist(self):
        print("Entering interactive mode...")
        user_input = "no"
        while user_input != "3":
            user_input = input("Please select one of the three options: \n1: Add a song to the playlist\n2: Remove a song from the playlist\n3: Exit interative mode (accept playlist)\n - ")
            if user_input == "1":
                self.addSong()
            elif user_input == "2":
                self.removeSong()
            else:
                return
        
    def addSong(self):
        song_name = input("Please enter the songname of the song you want to add: ")
        artist = input("Please enter the artist of this song: ")
        self.playlist["playlist"].append((song_name, artist))
        print("Successfully added song! ")
    
    def removeSong(self):
        user_input = int(input("Please enter the number of the song you would like to remove (from above list): "))
        if user_input < 1 or user_input > len(self.playlist["playlist"]): 
            print("You have entered an invalid song index!")
        else:
            song = self.playlist["playlist"].pop(user_input - 1)
            print("Successfully removed: {}".format(song))

    '''
    Returns 5 random songs from [timeframe] month from listening_history.json
    '''
    def getListeningHistory(self):
        songlist = []
        if (self.args.timeframe == None):
            return 
        with open("Models/listening_history.json", "r") as history_file:
            history = json.load(history_file)[str(self.args.timeframe)]
            inc = 0
            while (inc < 5):
                rand = random.randint(0, len(history) - 1)
                song = history[rand]
                if (song["trackName"] != "Unknown Track"):
                    songlist.append((song["trackName"], song["artistName"]))
                    inc += 1
        self.playlist["timeframe"] = songlist

    def getGenres(self):
        assert(self.args.genre != None)
        genres = []
        with open("Models/genres.txt", "r") as genres_file:
            genres_full_list = genres_file.readlines()
            for i in range(0, len(genres_full_list), 3):
                title = genres_full_list[i].strip()
                description = genres_full_list[i + 1].strip()
                genres.append((title, description))
        self.playlist["genres"] = random.sample(genres, self.args.genre)
                
    def getWorldMusic(self):
        if (self.args.world == False):
            return
        country, decade = "", ""
        country = random.choice(list(open("Models/countries.txt"))).rstrip()
        decade = random.choice(list(open("Models/decades.txt"))).rstrip()
        self.playlist["world"] = [country, decade]

    def getArtist(self):
        if (self.args.artist == None):
            return
        self.playlist["artist"] = self.args.artist

    def getYear(self):
        if (self.args.year == None):
            return
        self.playlist["year"] = self.args.year
    
    def setMood(self):
        if (self.args.mood == None):
            return
        self.playlist["mood"] = self.args.mood
    
    def getGPTRecommendations(self):
        mood = self.playlist["mood"] if self.args.mood else None
        verbose = True if self.args.verbose else False

        prompter = Prompter(mood, verbose)
        if "genres" in self.playlist: self.playlist["genres"] = prompter.ask_chatgpt("genres", self.playlist["genres"])
        if "artist" in self.playlist: self.playlist["artist"] = prompter.ask_chatgpt("artist", self.playlist["artist"])
        if "world" in self.playlist: self.playlist["world"] = prompter.ask_chatgpt("world", self.playlist["world"])
        if "year" in self.playlist: self.playlist["year"] = prompter.ask_chatgpt("year", self.playlist["year"])

    def shuffledPlaylist(self):
        if "playlist" in self.playlist:
            playlist = self.playlist["playlist"]
            random.shuffle(playlist)
            return playlist
        else:
            return None
    
    # Sets a playlist as list of <songname - artist> (into self.playlist["playlist"])
    # This is useful if interactive mode is on
    def setPlaylist(self):
        playlist = []
        modes = ["timeframe", "genres", "artist", "world", "year"]
        for mode in modes:
            if mode in self.playlist:
                for song in self.playlist[mode]:
                    playlist.append(song)

        self.playlist["playlist"] = playlist

    def generatePlaylist(self):
        self.getListeningHistory()
        self.getGenres()
        self.getWorldMusic()
        self.getArtist()
        self.getYear()
        self.setMood()
        self.printExtendedPlaylist()

    def generate(self):
        user_input = "no"
        while (user_input != ""):
            self.generatePlaylist()
            user_input = input("Press enter to accept this playlist seed or type in any character to regenerate: ")
        
        self.getGPTRecommendations()
        self.setPlaylist()
        self.printPlaylist()

        if self.args.output: self.savePlaylist(self.args.output)
        if self.args.interactive: self.interactivePlaylist()

        return self.shuffledPlaylist()

    def sample_playlist(self):
        self.playlist["world"] = [("Oh The Sunn!", "The Avalanches"), ("Memory Box", "Peter Cat Recording Co.")]
        self.playlist["artist"] = [("Out Getting Ribs", "King Krule"), ("Toy", "Young Fathers")]
        self.playlist["timeframe"] = [("Hands Away", "Interpol"), ("Something For Your M.I.N.D.", "Superorganism")]

        self.setPlaylist()
        
        return self.shuffledPlaylist()