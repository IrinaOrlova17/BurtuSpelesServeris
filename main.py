import json
from flask import Flask, request, jsonify
app = Flask('app')

@app.route('/rezultati')
def rezultati():
  with open("rezultati.json", "r", encoding="utf-8") as f:
    dati = json.loads(f.read())
  sakartotiDati = sorted(dati, key = byLaiks_key)
  while len(sakartotiDati)>10:
    sakartotiDati.pop()
  return jsonify(sakartotiDati)

@app.route('/speletaja-rezultats', methods = ['POST'])
def speletajaRezultats():
  rez = request.json        #serveris saņem
  with open("rezultati.json", "r", encoding="utf-8") as f:
    dati = json.loads(f.read())
  dati.append(rez)

  with open("rezultati.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(dati, indent =2))
  return jsonify(dati)

def byLaiks_key(speletajs):
    return speletajs["laiks"]
  
app.run(host='0.0.0.0', port=8080)
