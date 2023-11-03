import json
import requests

"""
Con este código se hace el llamado a la API y se obtienen las palabras de allí 

"""


def get_random_word(length):
    random_word_api_url = "https://random-word-api.herokuapp.com/word"
    random_word_api_response = requests.get(
        random_word_api_url, params={"length": length, "lang": "en"})
    randomword = random_word_api_response.json()[0]
    return randomword


def get_word_definition(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"
    response = requests.get(url.format(word))
    return response


def get_randoms_words_with_meanings(length):
    words = {}
    for _ in range(101):
        status_code = 404
        while status_code != 200:
            word = get_random_word(length)
            meaning_response = get_word_definition(word)
            status_code = meaning_response.status_code
        definition = meaning_response.json()[0]["meanings"][0]["definitions"][0]["definition"]
        words[word] = word
        words[f'{word} definition'] = definition
    return words
