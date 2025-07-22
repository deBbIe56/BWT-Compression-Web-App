from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def bwt_transform(s):
    s += '$'
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = [row[-1] for row in table]
    return ''.join(last_column)

@app.route('/compress', methods=['POST'])
def compress():
    data = request.get_json()
    dna = data.get('dna', '')
    if not dna:
        return jsonify({'error': 'No DNA provided'}), 400
    compressed = bwt_transform(dna)
    return jsonify({'compressed': compressed})

if __name__ == '__main__':
    app.run(debug=True)