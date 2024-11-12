from flask import Flask, request, jsonify
from functions import *

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "API is working"

@app.route('/pdf-process', methods = ['POST'])
def pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF part"}), 400

    pdf_file = request.files['pdf']
    processPDF(pdf_file)
    return jsonify({"message": "File processed successfully"}), 200

@app.route('/url-process', methods = ['POST'])
def url():
    if 'url' not in request.json:
        return jsonify({'error': "No URL found"}), 400
    processURL(request.json['url'])
    return jsonify({'message': 'URL data processes successfully'}), 200

@app.route('/get-response', methods = ['POST'])
def get_result():
    if 'query' not in request.json:
        return jsonify({'error': 'No query received'}), 400
    query = request.json['query']
    result = get_response(query)
    return jsonify({'message': result}), 200

if __name__ == '__main__':
    app.run(debug=True)