import json
from difflib import get_close_matches
import os

data_file_path = os.path.join("data", "7.1 data.json")
with open(data_file_path, "r") as file:
    data = json.load(file)


def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("DID YOU MEAN %s?" % get_close_matches(word, data.keys())[0])
        tell = input("press y for yes or n for no: ")
        if tell == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif tell == "n":
            return "Error in word"
        else:
            return "word not found"
    else:
        return "Word not found in dictionary"
