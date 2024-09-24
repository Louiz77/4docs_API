from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from services.file_service import FileService
from config import APIConfig

file_blueprint = Blueprint('file_blueprint', __name__)

@file_blueprint.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file.content_type != 'application/pdf':
        return jsonify({"error": "File must be a PDF"}), 400

    try:
        api_config = APIConfig()
        auth_service = AuthService(api_config)
        file_service = FileService(api_config)

        access_token = auth_service.get_access_token()
        result = file_service.send_file_to_4docs(file, access_token)
        return jsonify(result), 200 if 'error' not in result else 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
