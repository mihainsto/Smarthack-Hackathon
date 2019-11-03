from flask import Flask, request, json, jsonify
from flask_cors import CORS

import gensim
import gensim.models.keyedvectors as word2vec

print('test')
print('Started loading')
MODEL_PATH = 'GoogleNews-vectors-negative300.bin'
model =  word2vec.KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)
print('Done')

app = Flask(__name__)
CORS(app)

# @app.before_first_request
# def activate_job():
# 	print('Started loading')
# 	MODEL_PATH = 'GoogleNews-vectors-negative300.bin'
# 	model =  word2vec.KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)
# 	print('Done')

@app.route('/')
def index():
	print(similarity(descriere = 'Donez combina frigorifica', cautare = 'frigider', treshold = 0.4))
	return 'Hello There!'

# @app.route('/sim', methods=['POST'])
# def sim():
#     if request.method == 'POST':
#         userDetails = request.json
#         print(userDetails)
#         print('\n')
#         text = userDetails['text']
#         word_sim = userDetails['word_sim']
#         return '1'
#         #return similarity(str(text),str(word_sim),0.4)


# @app.route('/auth', methods=['POST'])
# def auth():
#     if request.method == 'POST':
#         userDetails = request.json
#         print(userDetails)
#         username = userDetails['username']
#         password = userDetails['password']
#         return 1

@app.route('/simget/<string:text>/<string:word_sim>', methods=['GET'])
def simget(text, word_sim):
  text = text.replace('_',' ')
  word_sim = word_sim.replace('_',' ')
  print(text)
  sim = similarity(str(text),str(word_sim),0.4)
  return jsonify({'stauts':str(sim)}) 

def ro_to_eng(ro_text):
	from googletrans import Translator
	translator = Translator()
	eng_text = translator.translate(ro_text, src='ro')
	return eng_text.text
  
def similarity (descriere, cautare, treshold):
  # text = text.lower()
  print("ORIGINAL", descriere)
  descriere = ro_to_eng(descriere)
  print ("TRADUS",descriere)
  import string
  exclude = set(string.punctuation)
  aux = []
  for ch in descriere:
    if ch not in exclude:
      aux.append(ch)
    else:
      aux.append(' ')
  descriere = ''.join(aux)
  descriere = descriere.split(" ")
  print ("DUPA SPLIT", descriere)
  #pana aici scoate punctuatia pentru primul text
  # word_sim = word_sim.lower()
  print ("ORIGINAL", cautare)
  cautare = ro_to_eng(cautare)
  print ("TRADUS", cautare)
  aux = []
  for ch in cautare:
    if ch not in exclude:
      aux.append(ch)
    else:
      aux.append(' ')
  cautare = ''.join(aux)
  cautare = cautare.split(" ")
  print ("DUPA SPLIT", cautare)
  for cuvant_cautat in cautare:
    matchuri = []
    for cuvant_descriere in descriere:
      scor = -1
      try:
        scor = model.similarity(cuvant_cautat,cuvant_descriere) #exista in dictionar
      except:
        if cuvant_cautat == cuvant_descriere: #nu exista in dictionar, dar se potriveste
          scor = 1
        else: #nu exista in dictionar, nici in descriere
          scor = -1
      matchuri.append(scor)
    if max(matchuri) < treshold:
      print (max(matchuri))
      return False
  return True












