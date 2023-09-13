import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

lemmmatizer = WordNetLemmatizer()
try:
    with open('intents.json') as file:
        intents = json.load(file)
except json.JSONDecodeError as e:
    print("Error al decodificar el archivo JSON:", str(e))

#words = pickle.load(open('words.pkl', 'rb'))
#clases = pickle.loads(open('clases.pkl', 'rb'))
with open('words.pkl', 'rb') as words_file:
    words = pickle.load(words_file)
with open('clases.pkl', 'rb') as clases_file:
    clases = pickle.load(clases_file)
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    long = len(words)
    bag = [0]*long
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res == np.max(res))[0][0]
    category = clases[max_index]
    return category

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"]==tag:
            result= random.choice(i['responses'])
            break
    return result
while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)



