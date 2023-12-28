import json
'''
Generates json file from Spotify JSON data to the following form
[
    "01": [{"songname" _:, "artist": _}, {"songname": _, "artist": _}]
]
'''
file_path = "/Users/anishkochhar/Documents/Imperial/Year Three/General/Spotify Data/Spotify Account Data/"
file_list = ["StreamingHistory0.json", "StreamingHistory1.json", "StreamingHistory2.json",
             "StreamingHistory3.json", "StreamingHistory4.json", "StreamingHistory5.json"]


if __name__ == '__main__':
    history = {}
    # Read JSON data from files
    for file_name in file_list:
        with open(file_path + file_name, "r") as file:
            data_dict = json.load(file)
            for entry in data_dict:
                if (entry["msPlayed"] < 1000): continue
                if (entry["artistName"] == "Unknown Artist"): continue
                if (entry["trackName"] == "Unknown Track"): continue
                month = int(entry["endTime"].split("-")[1])
                new_entry = {}
                new_entry["artistName"] = entry["artistName"]
                new_entry["trackName"] = entry["trackName"]
                if month not in history:
                    history[month] = []
                history[month].append(new_entry)

    # Write to json files
    with open("Models/listening_history.json", "w") as output_file:
        json.dump(history, output_file, indent='\t')