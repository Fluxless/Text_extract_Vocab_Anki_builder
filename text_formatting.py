import re
import mobi
import os
import requests
import json
import xml.etree.ElementTree as ET
import pprint as pprint
import csv

def extract_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return list(set(words))


def map_words(book_vocab, lang_dict):
    translated_vocab = {}
    for word in book_vocab:
        translation = lang_dict.get(word)
        if translation:  
            translated_vocab[word] = translation
    return translated_vocab




def main():
    #text = 'r'+ input("Enter file location:")
    with open('test_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    ##lang_dict = input("Enter Language: Swedish, (more to be added later if this is cool enough to continue)") # Make a function with switch statement to select lang. Or be lazy and if/else it
    with open('swedish_english_translations.json', 'r') as file:
        lang_dict = json.load(file)
    book_vocab = extract_words(text)
    print(book_vocab)

    translated_vocab = map_words(book_vocab, lang_dict)

    print("Test break block")
    pprint.pprint(translated_vocab)

    with open('output_anki.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in translated_vocab.items():
            writer.writerow([key, value])
if __name__ == "__main__":
    main()