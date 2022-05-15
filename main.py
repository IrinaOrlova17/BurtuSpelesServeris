import json
import os
import random
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask('app')
CORS(app)

@app.route('/spele/rezultati')
def rezultati():
  with open("rezultati.json", "r", encoding="utf-8") as f:
    dati = json.loads(f.read())
  sakartotiDati = sorted(dati, key = byLaiks_key)
  while len(sakartotiDati)>10:
    sakartotiDati.pop()
  return jsonify(sakartotiDati)

@app.route('/spele/speletaja-rezultats', methods = ['POST'])
def speletajaRezultats():
  rez = request.json        #serveris saņem
  with open("rezultati.json", "r", encoding="utf-8") as f:
    dati = json.loads(f.read())
  dati.append(rez)

  with open("rezultati.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(dati, indent =2))
  return jsonify(dati)

@app.route('/spele/random-vards')
def randomVards():
  with open("vardi.json", "r", encoding="utf-8") as f:
    dati = json.loads(f.read())
  randomIndex = random.randint(0, len(dati)-1)
  return dati[randomIndex]

def byLaiks_key(speletajs):
    return speletajs["laiks"]
  
# @app.route('/chat/lasit')
# def lasit():
#   with open('chat.json','r', encoding="utf-8") as f:
#     chat = f.read()
    
#   return chat

# @app.route('/chat/sutit/<vards>/<zina>')
# def sutit(vards, zina):
#   tagad = datetime.now()
#   laiks = tagad.strftime("%Y-%m-%d, %H:%M:%S")
 
#   print(laiks)
  
#   rinda = {
#         "zina":zina,
#         "vards":vards,
#         "laiks":laiks
#   }
#   with open('chat.json','r', encoding="utf-8" ) as r:
#     vecie = r.read()
#     rindas = json.loads(vecie)

#   if vards == "Serveris":
#     rinda["vards"] = "Nu-nu-nu!"
  
#   if zina == "!stats":
#     chata_garums = len(rindas)
#     rinda["zina"] = "Čatā ir " + str(chata_garums) + " ieraksti."
#     rinda["vards"] ="Serveris"
    
#   rindas.append(rinda)

#   with open('chat.json','w', encoding="utf-8") as f:
#     f.write(json.dumps(rindas, indent=2, ensure_ascii=False))

#   return "Ok"

app.run(host='0.0.0.0', port=8080)