from flask import Blueprint, request, jsonify
from .services import get_access_token, send_file_to_4docs

app = Blueprint('routes', __name__)

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file.content_type != 'application/pdf':
        return jsonify({"error": "File must be a PDF"}), 400

    try:
        access_token = get_access_token()
        result = send_file_to_4docs(file, access_token)
        return jsonify(result), 200 if 'error' not in result else 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
