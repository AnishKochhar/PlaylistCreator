import json, random, textwrap
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
    '''
    Returns 5 random songs from [timeframe] months ago from my listening history
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
    
    def getGPTRecommendations(self):
        prompter = Prompter(self.playlist)
        self.playlist["genres"] = prompter.ask_chatgpt("genres", self.playlist["genres"])
        self.playlist["artist"] = prompter.ask_chatgpt("artist", self.playlist["artist"])
        self.playlist["world"] = prompter.ask_chatgpt("world", self.playlist["world"])

    def getFullPlaylist(self):
        playlist = []
        for songlist in self.playlist.values():
            playlist += songlist
        random.shuffle(playlist)
        return playlist

    def generatePlaylist(self):
        self.getListeningHistory()
        self.getGenres()
        self.getWorldMusic()
        self.getArtist()
        self.printExtendedPlaylist()

    def generate(self):
        user_input = "no"
        while (user_input != ""):
            self.generatePlaylist()
            user_input = input("Press enter to accept these .. or type in any character to regenerate: ")
        
        self.getGPTRecommendations()
        self.printPlaylist()

        return self.getFullPlaylist()

    def sample_playlist(self):
        self.playlist["world"] = [("Oh The Sunn!", "The Avalanches"), ("Memory Box", "Peter Cat Recording Co.")]
        self.playlist["artist"] = [("Out Getting Ribs", "King Krule"), ("Toy", "Young Fathers")]
        self.playlist["timeframe"] = [("Hands Away", "Interpol"), ("Something For Your M.I.N.D.", "Superorganism")]

        return self.getFullPlaylist()