import random
import json
import pickle
import numpy as np
#para func sintacticas
import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

#intents = json.loads(open('intents.json').read())
try:
    with open('intents.json') as file:
        intents = json.load(file)
except json.JSONDecodeError as e:
    print("Error al decodificar el archivo JSON:", str(e))

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

words = []
clases = []
documents= []
ignore_letters = ['?',';',',','.']

for intents in intents['intents']:
    for pattern in intents['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list , intents["tag"]))
        if intents["tag"] not in clases:
            clases.append(intents["tag"])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters ]
word = sorted(set(words))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(clases, open('clases.pkl', 'wb'))

training = []
output_empty = [0]*len(clases)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty) 
    output_row[clases.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)

print(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(learning_rate=0.001, decay=1e-6, momentum=0.9, nesterov= True )
model.compile(loss='categorical_crossentropy', optimizer= sgd, metrics= ['accuracy'])
train_process = model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=5, verbose=1)
model.save("chatbot_model.h5", train_process)
