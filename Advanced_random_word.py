import random
import json
import requests


#number_of_words = int(input("How many words would you like to print?"))

answer = input("Do you want to print a random word? ")

api = "https://api.dictionaryapi.dev/api/v2/entries/en/"

if answer == "Y" or answer == "y":


    my_dict_from_file = json.load(open("D:\Python CoderDojo\Random word generator\Random word generator with definition\words_dictionary.json", "r"))

    #my_list = ["computer", "Gold", "List", "Road", "Table", "Bottle"]

    word_list = list(my_dict_from_file.keys())

    #for i in range(0,number_of_words):
    word = random.choice(word_list)
    print(word)
    response = requests.get(api + word)

    try:
        print(response.json()[0]["meanings"][0]["definitions"][0]["definition"])
    except:
        print("No such definition")


