from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def test():
    info = requests.get('http://localhost:5000/')
    text = info.json()
    odp = f"<p>Wykonawka: {text['performer']}</p><p>Albumy: {text['albums'][0]}" \
          f", {text['albums'][1]}</p><p>Piosenki: "
    for i in text['songs']:
        odp += f"<p>{i['name']}, format: {i['format']}</p>"
    odp += "</p>"
    return odp


if __name__ == '__main__':
    app.run(debug=True, port=80)
